#!/usr/bin/env python
# _*_coding:utf-8_*_

import MySQLdb
import conf


class MysqlHelper(object):
    def __init__(self, instance='zabbix'):
        dict_instance1 = 'conn_dict_{}'
        dict_instance = dict_instance1.format(instance)
        self.__conn_dict = getattr(conf, dict_instance)

    def get_dict(self, sql, tablelist):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        cur.execute(sql, tablelist)
        data = cur.fetchall()

        cur.close()
        conn.close()

        return data

    def get_one(self, sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        cur.execute(sql)
        data = cur.fetchone()

        cur.close()
        conn.close()

        return data
