#!/bin/env python
import sys, os
import subprocess
import timeit
import datetime

log_file = '/home/anand/.sys_entropy.log'

out_fd = open(log_file,'a',0)

def main():
    date = datetime.datetime.utcnow()
    out_fd.write("Date: %s\n"%date)

    uptime_proc = subprocess.Popen('uptime',stdout=out_fd)

    #Available entropy from the /proc fs
    proc_fd = open('/proc/sys/kernel/random/entropy_avail')
    avail_entropy = int(proc_fd.read().strip('\n'))
    proc_fd.close()
    out_fd.write("\nAvailable entropy value(from procfs):%s\n"%avail_entropy)

    t = timeit.Timer(os_system_dd)
    out_fd.write("Timer output: %f"%t.timeit(1))
    os.remove('/home/anand/sys_entropy_random')
    out_fd.close()

def os_system_dd():
    global out_fd
    out_fd.write("executing the time dd command\n")
    cmd_list = ['dd','if=/dev/random', 'of=/home/anand/sys_entropy_random', 'bs=1M' ,'count=500']
#    subprocess.call(cmd_list,stdout=out_fd)
    #import pdb;pdb.set_trace()
    proc = subprocess.Popen(cmd_list,stdout = out_fd,stderr=out_fd)
    proc.wait()



if __name__ == '__main__':
    print __name__
    main()
