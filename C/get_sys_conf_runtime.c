#include <unistd.h>
#include <string.h>
#include <stdio.h>

int main(int argc,char* argv[])
{
    int i;
    printf("%ld\n",sysconf(_SC_ATEXIT_MAX));
    for (i=1;i<argc;i++){
    printf("%s:%ld\n",argv[i],sysconf(argv[i]));
    }

}

