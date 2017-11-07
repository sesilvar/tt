#!/usr/bin/env python
# _*_coding:utf-8_*_


from wsgiref.simple_server import make_server, demo_app


appl = demo_app
server = make_server('127.0.0.1', 8000, appl)

server.handle_request()
