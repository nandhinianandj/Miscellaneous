/**
 * simple.c
 */
#include <stdio.h>
#include <stdlib.h>

#define NSIZE 200000000

char x[NSIZE];
int main (void)
{
  for (int i=0; i < NSIZE; i++)
    x[i] = 'x';

  printf ("done\n");
  exit (EXIT_SUCCESS);

}
