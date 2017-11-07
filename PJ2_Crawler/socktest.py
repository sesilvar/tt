#!/usr/bin/env python
# _*_coding:utf-8_*_


import socket


def tcpserver():
    socktcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socktcp.bind(('localhost', 8000))
    socktcp.listen(5)

    while True:
        clienttcp, address = socktcp.accept()
        recc = clienttcp.recv(1024)
        clienttcp.send('HTTP/1.1 200 OK\r\n\r\n')
        clienttcp.send('Hello!')
        print recc
        clienttcp.close()


if __name__ == '__main__':
    tcpserver()
