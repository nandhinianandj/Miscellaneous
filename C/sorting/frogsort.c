#include <stdio.h>
//#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/wait.h>
#include <time.h>

#include "debug.h"
#define MAX_LIMIT 50



long int* frogsort(long int* input)
{
    int w=0, status=0;
    struct timespec req,rem;
    pid_t pid;
    pid_t child_pids[MAX_LIMIT];
    long int sleep_time, *temp,ret_value,ret_val;

    int i =0,ret;
    int **pipefd;
    do 
    {   
        pipe(pipefd[i]);
        switch(pid = fork())
        {
            case -1:
                perror("fork failed");
                exit(1);

            case 0:
                child_pids[i] = getpid();
                sleep_time = input[i];
                req.tv_sec = 0;
                req.tv_nsec = sleep_time;
                printf("Child process(pid): %d\n sleeping for:%ld\n",child_pids[i],sleep_time);
                nanosleep(&req,&rem);
                write(pipefd[i][1],&sleep_time,sizeof(sleep_time));
                close(pipefd[i][1]);
                exit(req.tv_nsec);
            default:
                do {
                    w = waitpid(pid,&status,WUNTRACED |WCONTINUED);
                    if (WIFEXITED(status)) {
                         printf("exited, status=%d\n", WEXITSTATUS(status));
                         ret = read(pipefd[i][0],&ret_value,sizeof(ret_value));
                         close(pipefd[i][0]);
                    } else if (WIFSIGNALED(status)) {
                         printf("killed by signal %d\n", WTERMSIG(status));
                    } else if (WIFSTOPPED(status)) {
                         printf("stopped by signal %d\n", WSTOPSIG(status));
                    } else if (WIFCONTINUED(status)) {
                         printf("continued\n");
                    }
                    //temp[i] = ret_value;
                } while (!WIFEXITED(status) && !WIFSIGNALED(status));
        }
    i++;
    }while (*(input++));
    
return  temp;
    
}


int main(int argc,char **argv)
{
    unsigned long int input[MAX_LIMIT], *output;
    int arg_len;
    int i=0;
    check(argc >=2,"Sorry argument necessary"); 
    arg_len = argc;
    printf("No of arguments passed: %d\n",arg_len);
    malloc(sizeof(long int) *arg_len-1);
    for(i=0;i<arg_len-1;i++){
        input[i] = atol(argv[i+1]);
        
        printf("%ld\n",input[i]);
    }
    output = frogsort(input);
    for(i=0;i<arg_len-1;i++)
    printf("Sorted result: %ld\n",output[i]);
error:
    return 1;
}
