# -*- encoding: utf-8 -*-


import sys
import xlrd
import time
import datetime
import logging


def str_to_date(item, ctype = 1):
    '''用于将excel中的字符串转化为date对象'''

    if ctype == 3:
        return xlrd.xldate.xldate_as_datetime(item, 0)

    #支持4种格式的字符串
    #1、2019/08/09
    #2、2019-08-09
    #3、2019/08/09 10:00:30
    #4、2019-08-09 10:00:30
    date_spliter = '/'
    time_spliter = ':'
    if u'-' in item.decode('utf-8'):
        date_spliter = '-'

    tokens = item.split(' ')

    if len(tokens) < 1:
        return None

    date_str = tokens[0].rstrip('-').rstrip('/')
    date_tokens = date_str.split(date_spliter)

    if len(date_tokens) < 3:
        return None

    year = int(date_tokens[0])
    month = int(date_tokens[1])
    day = int(date_tokens[2])
    hour = 0
    min = 0
    sec = 0

    if len(tokens) >= 2:
        time_str = tokens[1]
        time_tokens = time_str.split(time_spliter)
        if len(time_tokens) == 3:
           hour = int(time_tokens[0])
           min = int(time_tokens[1])
           sec = int(time_tokens[2])
        else:
           hour = int(time_tokens[0])
           min = int(time_tokens[1])
    tm_str = "%04d%02d%02d%02d%02d%02d" % (year, month, day, hour, min, sec)
    st_tm = time.strptime(tm_str, "%Y%m%d%H%M%S")
    return datetime.datetime.fromtimestamp(time.mktime(st_tm))


def read_excel(inFileName):
    wb = xlrd.open_workbook(inFileName)
    table = wb.sheets()[0]

    rowLength = table.nrows

    lineCount = -1
    a = []
    for row in range(1, rowLength):  # 跳过表头
        lineCount += 1

        reportTime = str_to_date(table.row(row)[1].value, table.cell(row, 1).ctype)
        if reportTime == None:
            continue

        reportTime = reportTime.strftime('%Y%m%d%H%M%S')
        desc = table.row(row)[3].value

        d = {}
        d[u'sourceType'] = u'0'
        d[u'description'] = desc
        d[u'sourceId'] = u'0'
        d[u'reportTime'] = reportTime
        d[u'repeatId'] = u"0"
        d[u'intel_id'] = lineCount
        d[u'intel_ver'] = u"0"

        a.append(d)
    return a


def read_excel_all(inFileName):
    wb = xlrd.open_workbook(inFileName)
    sheets = wb.sheet_names()
    tables = [wb.sheet_by_name(x) for x in sheets]
    values = [[table.row_values(x) for x in range(0, table.nrows)] for table in tables]
    cups = zip(sheets, values)
    return dict(cups)


def read_excel_sheet(inFileName, sheet):
    wb = xlrd.open_workbook(inFileName)
    table = wb.sheet_by_name(sheet)

    rts = [table.row_values(x) for x in range(0, table.nrows)]
    return rts
