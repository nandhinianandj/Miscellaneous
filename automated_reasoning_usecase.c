#include<stdio.h>
#include<stdbool.h>
#include<limits.h>

bool f(unsigned int x, unsigned int y) {
   return (x+y == y+x);
}

void main() {
   for (unsigned int x=0;1;x++) {
      for (unsigned int y=0;1;y++) {
         if (!f(x,y)) printf("Error!\n");
         if (y==UINT_MAX) break;
      }
      if (x==UINT_MAX) break;
   }
}
