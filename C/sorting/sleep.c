#include "debug.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include <sys/wait.h>
#include <time.h>

struct sleep_time_struct
{
    struct timespec req;
    struct timespec rem;
};

long int sleep_and_ret(long int sleep_time)
{
 
    struct sleep_time_struct slts;

    pid_t child_pid;
    struct timespec req,rem;
    req.tv_sec = 0;
    req.tv_nsec = sleep_time;
    child_pid = getpid();
    printf("Child process(pid): %d\n sleeping for:%ld\n",child_pid,sleep_time);
    nanosleep(&req,&rem);
    return sleep_time;
}

long int main(int argc, char **argv)
{
    
    long int slpt;
    check(argc >=2,"Sorry argument necessary"); 
    slpt = atol(argv[1]); 
    return sleep_and_ret(slpt);

    error:
        return 1;
}

