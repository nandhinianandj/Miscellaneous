#!/bin/env python
import sys, os
import subprocess
import timeit
import datetime
import json


log_file = '/home/anand/.sys_entropy/.sys_entropy.log'
log_fd = open(log_file,'a',0)

res_file = '/home/anand/.sys_entropy/sys_entropy'
res_fd = open(res_file,'a',0)

def main():
    out_dict = dict()
    date = datetime.datetime.utcnow()
    out_dict.update({'Date:':date})
    log_fd.write("\n Date: %s\n"%date)


    uptime_proc = subprocess.Popen('uptime',stdout=log_fd)

    #Available entropy from the /proc fs
    proc_fd = open('/proc/sys/kernel/random/entropy_avail')
    avail_entropy = int(proc_fd.read().strip('\n'))
    proc_fd.close()
    out_dict.update({'Available entropy(procfs)':avail_entropy})
    log_fd.write("Available entropy value(from procfs):%s\n"%avail_entropy)

    t = timeit.Timer(os_system_dd)
    t_result = t.timeit(1)
    out_dict.update({'Timer result':t_result})
    log_fd.write("Timer output: %f\n"%t_result)
    res_fd.write(json.dumps(out_dict))
    os.remove('/home/anand/sys_entropy_random')
    log_fd.close()
    res_fd.close()

def os_system_dd():
    global log_fd
    log_fd.write("executing the time dd command\n")
    cmd_list = ['dd','if=/dev/random', 'of=/home/anand/sys_entropy_random', 'bs=1M' ,'count=500']
    proc = subprocess.Popen(cmd_list,stdout = log_fd,stderr=log_fd)
    proc.wait()



if __name__ == '__main__':
    print __name__
    main()
