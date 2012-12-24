#include <stdio.h>
#include <time.h>
void main(){
    struct timespec test,rem;
    int ret;
    //long int p = 5*1000000000000;
    test.tv_sec = 0;
    test.tv_nsec = 5*10000;
    ret = nanosleep(&test,&rem);
    printf("Thanks for the nap: %d \n",ret);
}
