#include <stdlib.h>
typedef struct testA
{
    int a;
    float b;
    char *c;
}test;

void main()
{
    test *A,*B;

    A->a = 5;
    A->b= 12.0;
    A->c = "eue";

    //B = malloc(sizeof(test));
    B = (void*) A;

    printf("%d\t %f \t %s \n ",B->a,B->b,B->c);
    //free(B);
}
