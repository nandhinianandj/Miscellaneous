#include <stdio.h>

int b(void) {puts("3");return 3;}
int c(void) {puts("4");return 4;}

int main(void)
{
    int a = b() + c();
    printf("%d \n",a);
}
