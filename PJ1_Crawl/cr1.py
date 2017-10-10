#!/usr/bin/env python
# _*_coding:utf-8_*_


from bs4 import BeautifulSoup
from urllib2 import HTTPError, urlopen


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return e
    try:
        bs1 = BeautifulSoup(html.read(), 'html.parser')
        title1 = bs1.title
    except AttributeError as e:
        return e
    return title1


mytitle = get_title('http://blog.csdn.net/cangchen/article/details/45673223')
print mytitle
