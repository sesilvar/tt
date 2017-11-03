#!/usr/bin/env python
# _*_coding:utf-8_*_


from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())


def getlinks(articleurl):
    html = urlopen('http://en.wikipedia.org' + articleurl)
    bs1 = BeautifulSoup(html, 'html.parser')
    return bs1.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getlinks('/wiki/Kevin_Bacon')

if len(links) > 0:
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']
    print newarticle
#    links = getlinks(newarticle)
