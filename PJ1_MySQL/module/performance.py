#!/usr/bin/env python
# _*_coding:utf-8_*_

from utility import sql_helper


class Performance(object):
    def __init__(self, instance):
        self.__helper = sql_helper.MysqlHelper(instance)

    def get_data_table(self, tablelist):
        sql = '''SELECT table_schema,table_name,table_rows,
ROUND(data_length/1024/1024,2) AS 'data_length(MB)',
ROUND(index_length/1024/1024,2) AS 'index_length(MB)',
ROUND(data_free/1024/1024,2) AS 'data_free(MB)',
update_time 
FROM information_schema.tables 
WHERE table_schema NOT IN ('mysql','sys','information_schema','performance_schema') 
AND table_name IN (%s,%s,%s,%s,%s); '''

        return self.__helper.get_dict(sql, tablelist)

    def get_status_one(self, params):
        sql1 = 'show global status like "%{}%";'
        sql = sql1.format(params)

        return self.__helper.get_one(sql)
