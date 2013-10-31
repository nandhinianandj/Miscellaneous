#include <stdio.h>

void print_facts(int num1, int num2);
int max_of_two(int j, int k);
double avg_of_two(int c, int d);

int main(void)
{
    int i;
    int j;
    /* point 1*/
    i = -8;
    j = 7;

    /*point 2*/
    print_facts(i,j);
    /* point 10 */
    return 0;

}

void print_facts(int num1, int num2)
{
    int larger;
    double the_avg;

    /* point 3 */
    larger = max_of_two(num1,num2);

    /* point 6 */
    the_avg = avg_of_two(num1,num2);

    /*point 9 */
    printf("For the tow integers %d and %d, \n",num1,num2);
    printf("the larger is %d and the average is %g. \n",larger,the_avg);

}

int max_of_two(int j, int k)
{
    /* point 4 */
    if (j < k)
        j = k;
    /* point 5 */
    return j;
}

double avg_of_two(int c, int d)
{
    double sum;
    /* point 7 */
    sum = c + d;
    /* point 8 */
    return (c+d) / 2.0;
}

