#!/bin/env python
import sys, os
import subprocess

log_file = '/home/anand/.sys_entropy.log'

def main():
    out_fd = open(log_file,'a')
    date_proc = subprocess.Popen('date')
    date = date_proc.communicate()
    out_fd.write("Date: %s",date)
    uptime_proc = subprocess.Popen('uptime')
    uptime = uptime_proc.communicate()
    out_fd.write("Uptime:%s",uptime)

    #Available entropy from the /proc fs
    proc_fd = open('/proc/sys/kernel/random/entropy_avail')
    avail_entropy = int(proc_fd.read().strip('\n'))
    proc_fd.close()
    out_fd.write("Available entropy value(from procfs):%s",avail_entropy)



if __name__ == '__prog__':
    main()
