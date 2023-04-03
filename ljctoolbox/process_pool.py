#!/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2019 TehFront inc. All rights reserved.
文件名称：process_pool.py
创 建 者：liujichao.ljc
邮    箱：liujichao.ljc@qq.com
创建日期：2019/11/19 15:34 
"""

import os, sys, traceback, logging, signal
from multiprocessing import Process, Pool, Manager, Event
from subprocess import Popen, PIPE, STDOUT


def commond_execute(cmd, num=0, logger=None):
    try:
        if logger is None:
            logger = logging

        sub = Popen(cmd, bufsize=1, shell=True, stdout=PIPE, stderr=STDOUT, preexec_fn=os.setsid, close_fds=True)
        while sub.poll() is None:
            l = sub.stdout.readline()
            if l:
                logger.info("[%s]:%s" % (num, l))
                sys.stdout.flush()
            else:
                break
    except Exception, e:
        logger.warn("faile to exe:[%s][%s][%s]" % (num, cmd, e))
        return False
    finally:
        try:
            os.killpg(sub.pid, signal.SIGKILL)
        except OSError, e:
            logging.warn("kill group failed gpid:[%s]" % sub.pid)
    return sub.wait() == 0


def worker(func, q, err, lock, param):
    try:
        ret = func(param)
        lock.acquire()
        q.put(ret)
    except Exception, e:
        err.put("[%s][%s]" % (e, traceback.format_exc()))
    finally:
        lock.release()


class ProPool(object):
    def __init__(self, num=5):
        self.pool = Pool(num)
        self.m = Manager()
        self.q = self.m.Queue()
        self.err = self.m.Queue()
        self.lock = self.m.Lock()

    def reset_pool_size(self, num):
        self.pool = Pool(num)

    @property
    def result(self):
        while not self.q.empty():
            yield self.q.get()

    @property
    def get_err(self):
        while not self.err.empty():
            yield self.err.get()

    def add_task(self, func, param):
        self.pool.apply_async(func=worker, args=(func, self.q, self.err, self.lock, param,))
        return True

    def add_tasks(self, func, params):
        [self.add_task(func, x) for x in params]

    def process_status(self):
        return self.q.qsize()

    def join(self):
        try:
            self.pool.close()
            self.pool.join()
        except Exception, e:
            self.close()

    def close(self):
        self.m.shutdown()
