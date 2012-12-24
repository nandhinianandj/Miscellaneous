#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/wait.h>
#include <time.h>

#include "debug.h"

#define MAX_LIMIT 50

int main(int argc,char **argv)
{
    long int input[MAX_LIMIT], output[MAX_LIMIT];
    int arg_len;
    int i=0;
    check(argc >=2,"Sorry argument necessary"); 
    arg_len = argc;
    printf("printing %d\n",arg_len);
    malloc(sizeof(long int) *arg_len-1);
    for(i=0;i<arg_len-1;i++){
        //printf("casting argument %s\n",argv[i+1]);
        input[i] = (long)argv[i+1];
        
        //printf("%ld\n",input[i]);
    }
    for(i=0;i<arg_len-1;i++){
        output[i] = int_fork(input[i]);
    }
    for(i=0;i<arg_len-1;i++)
    printf("Sorted result: %ld\n",output[i]);
error:
    return 1;
}

int int_fork(int sleep_time)
{
    int w, pid,status;
    struct timespec req,rem;
    pid = fork();
    check(pid > -1,"Sorry failed to create process");
    if (pid ==0)
    {
        // child part
        req.tv_sec = 0;
        req.tv_nsec = sleep_time;
        nanosleep(&req,&rem);
        return sleep_time;

    }
    else 
    {
        do {
            w = waitpid(pid,&status,WUNTRACED |WCONTINUED);
            if (WIFEXITED(status)) {
                 printf("exited, status=%d\n", WEXITSTATUS(status));
            } else if (WIFSIGNALED(status)) {
                 printf("killed by signal %d\n", WTERMSIG(status));
            } else if (WIFSTOPPED(status)) {
                 printf("stopped by signal %d\n", WSTOPSIG(status));
            } else if (WIFCONTINUED(status)) {
                 printf("continued\n");
            }
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    return  w;
    }

error:
    return 1;
}
