#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//double win = 0.5;
//
double win = 0.473684;

main(int argc, char **argv)
{
    int fortune = 0, i,bet = 1;
    double v;
    int randseed;

    struct tm *newtime;
    time_t ltime;
    time(&ltime);

    newtime = localtime(&ltime);
    randseed = newtime->tm_sec;

    printf("%%!PS-Adobe-2.0 EPSF-1.2\n");
    printf("%%%%Creator:Martingale\n");
    printf("%%%%BoundingBox: 0 0 1000 400\n");
    printf("%%%%EndComments\n");
    printf("0 200 translate\n");
    printf(".125 .1 scale\n");
    printf("1 setlinecap\n");
    printf("4 setlinewidth\n");
    printf("0 0 moveto 8000 0 lineto closepath stroke\n");
    printf("0 -2000 moveto 0 2000 lineto closepath stroke\n");

    unsigned short c[3] = {23, 45, 78};

    if (argc == 2) c[2] = atoi(argv[1]);
    else c[2] = randseed;
    seed48(c);

    for(i = 0;i < 8000; i++) {
        v = drand48();
        if (v < win) {
            fortune += bet; bet = 1;

        } else {
            fortune -= bet; bet = bet *2;
            if (bet > 128) bet = 1;
        }
        printf("%d %d moveto %d %d lineto closepath stroke\n",
                    i,fortune,i,fortune);
    }

    printf("showpage\n");

}
