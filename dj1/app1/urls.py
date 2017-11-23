#!/usr/bin/env python
# _*_coding:utf-8_*_


from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^$', view.index, name='index'),
]
