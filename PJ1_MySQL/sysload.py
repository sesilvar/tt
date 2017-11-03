#!/usr/bin/env python
# _*_coding:utf-8_*_

import paramiko
import datetime
from loadconf import hostname


def sysload(hname):
    hostload = {'cpustat': "uptime|awk '{print $8,$9,$10,$11,$12}'",
                'iostat': "iostat -d -m|sed -n '3,4p'|awk '{print $1,$3,$4}'",
                'memused': "free -m|grep -i 'mem'|sed -n '1,2p'",
                'diskused': "df -h|awk '{print $5,$6}'"}
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hname[1], port=hname[2], username=hname[3], password=hname[4])
    for i in hostload:
        stdin, stdout, stderr = ssh.exec_command(hostload[i])
        hostload[i] = stdout.read()
    ssh.close()
    return hname[0], hostload


tt = datetime.datetime.now().strftime('%Y%m%d-%H:%M')
flog = open('yunstat.txt', 'w')
flog.write('\n\n'+tt)
for j in hostname:
    hstname, hstload = sysload(j)
    flog.write('\n\n'+hstname+'\n\n')
    for s in hstload:
        flog.write('\n'+s+'\n')
        flog.write(hstload[s])
flog.close()
