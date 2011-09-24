#!/bin/env python
import sys, os
import subprocess
import timeit
import datetime

log_file = '/home/anand/.sys_entropy.log'

def main():
    out_fd = open(log_file,'a')
    date = datetime.datetime.utcnow()
    out_fd.write("Date: %s\n"%date)

    uptime_proc = subprocess.Popen('uptime',stdout=out_fd)

    #Available entropy from the /proc fs
    proc_fd = open('/proc/sys/kernel/random/entropy_avail')
    avail_entropy = int(proc_fd.read().strip('\n'))
    proc_fd.close()
    out_fd.write("\nAvailable entropy value(from procfs):%s\n"%avail_entropy)

    t = timeit.Timer(number=1)
    t.timeit(os_system_dd,number=1)
    os.remove('sys_entropy_random')
    out_fd.close()

def os_system_dd():
    subprocess.call('dd','if=/dev/random of=sys_entropy_random bs = 1M count = 500')


if __name__ == '__main__':
    print __name__
    main()
