/* fake ptrace() */
#include <stdio.h>

long ptrace(int x, int y, int z)
{
  printf("B-)\n");
  return 0;
}

