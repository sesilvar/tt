#!/usr/bin/env python
# _*_coding:utf-8_*_


import socket



socktcp = socket.socket()
socktcp.connect(('127.0.0.1',8000))
socktcp.send('sendtest')
print str(socktcp.recv(1024))
print str(socktcp.recv(1024))



