#!/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2017 TehFront inc. All rights reserved.
File  ：pack.py
Author：liujichao.ljc
Email ：liujichao.ljc@qq.com
Date  ：2017/1/14 17:08 BeiJing
'''

import os
import sys
import tarfile
import zipfile


def zip(target_dir, out_dir, filelist=''):
    try:
        filenames = []
        if isinstance(filelist,list):
            # todo: need the file lists
            pass
        else:
            if os.path.isfile(target_dir):
                filenames.append(target_dir)
            else :
                for root, dirs, files in os.walk(target_dir):
                    for name in files:
                        filenames.append(os.path.join(root, name))

            zf = zipfile.ZipFile(out_dir, "w", zipfile.ZIP_DEFLATED)
            for tar in filenames:
                arcname = tar[len(target_dir):]
                #print arcname
                zf.write(tar,arcname)
            zf.close()
        print >> sys.stderr, "zip compress finished!"
        return True
    except Exception, e:
        print >> sys.stderr, "[error] : %s" % e
        return False

def un_zip(file_name, tar_dir):
    """unzip zip file"""
    try:
        zip_file = zipfile.ZipFile(file_name)
        if os.path.isdir(tar_dir):
            print >> sys.stderr, "warn: up_zip dir is exsit!!"
        else:
            os.mkdir(tar_dir)
        for names in zip_file.namelist():
            zip_file.extract(names,tar_dir)
        zip_file.close()
        print >> sys.stderr, "un_zip finished!"
        return True
    except Exception,e:
        print >> sys.stderr, "[error] : %s" % e
        return False


def tgz(target_dir, out_dir, filelist='', cmd='w:gz'):
    try:
        filenames=[]
        if isinstance(filelist,list):
            # todo: need the file lists
            pass
        else:
            if os.path.isfile(target_dir):
                filenames.append(target_dir)
            else:
                for root, dirs, files in os.walk(target_dir):
                    for name in files:
                        filenames.append(os.path.join(root, name))
        tar = tarfile.open(out_dir, cmd)
        for name in filenames:
            arcname = name[len(target_dir):]
            tar.add(name,arcname)
        tar.close()
        return True
    except Exception,e:
        print >> sys.stderr, "[error] : %s" % e
        return False


def un_tgz(file_name, tar_dir, cmd='r:gz'):
    tar = tarfile.open(file_name, cmd)
    tar.extractall(tar_dir)
    tar.close()
    return True

def tar(target_dir, out_dir, filelist=''):
    return tgz(target_dir, out_dir, filelist, 'w:')

def un_tar(file_name, tar_dir):
    return un_tgz(file_name, tar_dir, 'r:')

if __name__ == '__main__':
    print 'testing'
    zip('..//logtools','..//init.zip')
    un_zip('..//init.zip','..//upzip')
    tgz('..//logtools','..//init.tar.gz')
    un_tgz('..//init.tar.gz','..//uptgz')
    tar('..//logtools','..//init.tar')
    un_tar('..//init.tar','..//uptar')


