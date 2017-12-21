#!/bin/bash

cpu_load5=`uptime|awk '{print $9}'|sed 's/,//'`
echo 'cpu_load_5:' $cpu_load5
mem_free=`free -m|grep Mem|awk '{print $NF}'`
echo 'mem_free:' $mem_free
disk_free=`df -hm /|grep sda| awk '{print $4}'`
echo 'disk_free:' $disk_free
time_now=`date '+%Y-%m-%d %H:%M:%S'`
echo 'time_now:' $time_now

sql="insert into tt.upload(cpu_load5,mem_free,disk_free,collect_time) value($cpu_load5, $mem_free, $disk_free, '$time_now');"
echo $sql

mysql -uroot -ppasswd -e "$sql"


CREATE TABLE `upload` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `cpu_load5` decimal(5,2) DEFAULT NULL,
  `mem_free` int(20) unsigned DEFAULT NULL,
  `disk_free` int(20) unsigned DEFAULT NULL,
  `collect_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
  );
  
