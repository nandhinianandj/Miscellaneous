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


    A = malloc(sizeof(test *));
    B = malloc(sizeof(test *));


    A->a = 5;
    A->b= 12.0;
    A->c = "eue";
    B = (void*) A;

    printf("%d\t %f \t %s \n ",B->a,B->b,B->c);
    free(A);
    free(B);
}
