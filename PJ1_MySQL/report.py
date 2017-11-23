#!/usr/bin/env python
# _*_coding:utf-8_*_


import csv


# with open('rett.csv', 'rb') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print row

with open('rett.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows('something')
    csv.