#!/usr/bin/env python
# _*_coding:utf-8_*_


from module import performance

soso = ['soso', ('t_inter', 't_module','holder1','holder2','holder3')]
params = ('thread', 'questions')


def getdata(usedb):
    dbname = eval(usedb)
    query = performance.Performance(dbname[0])
    tablelist = dbname[1]
    result_data = query.get_data_table(tablelist)
    result_status = []
    for i in params:
        status_one = query.get_status_one(i)
        result_status.append(status_one)

    print result_data
    print result_status

#def send


if __name__ == '__main__':
    getdata('soso')
