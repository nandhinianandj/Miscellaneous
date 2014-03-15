// Copied from http://unix.stackexchange.com/questions/18273/is-there-a-way-to-kick-kswapd-and-make-it-swap-out-pages
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc < 2)
          return 1;
              int megs = atoi(argv[1]);
                  if (megs <= 0)
                        return 2;
                            int i;
                                for (i=0; i<megs; i++) {
                                        void *data = malloc(1024*1024);
                                                memset(data, 1, 1024*1024);
                                                    }
                                                        getchar();
                                                            return 0;
                                                            }
