#!/usr/bin/env python


import xlwt
import time
import pymysql

today = time
item_name=['Processor load (15 min average per core)', 'Total memory', 'Available memory', 'Free inodes on $1 (percentage)', 'Free disk space on $1 (percentage)']

def zabbix_report(day=today):
	ip_list = ['10.10.8.202']
	book = xlwt.Workbook()
	sheet1 = book.add_sheet(day)
	for ip in ip_list:
		data = monitor_data(ip)
	row = 1
	col = 1
	for 

def monitor_data(ipaddr):
	item_name=['Processor load (15 min average per core)', 'Total memory', 'Available memory', 'Free inodes on $1 (percentage)', 'Free disk space on $1 (percentage)']
	sql_hostid = 'select hostid from interface where ip = %s;' %ipaddr
	conn = pymysql.connect(host='10.10.8.251', port=3306, user='zabbix', passwd='DC@72mon', db='zabbix')
	cursor = conn.cursor()
	cursor.execute(sql_hostid)
	hostid = cursor.fetchone()
	for items in item_name:
		sql_itemid = 'select itemid from items where hostid = %s and name = %s;' %(hostid,items)
		cursor.execute(sql_itemid)
		itemid=cursor.fetchall()
		for itemid in:
			sql_itemvalue = 'select * from trends where itemid='24617' and clock=(select max(clock) from trends where itemid=);'
			
if __name__='__main__':
	main()
