#include<iostream>
#include<stdlib.h>

#define f(n) (f##n)
#define ff(n) -n

int main(int argc,char * argv[])
{
    if (argc >2)
    {
        std::cout << "error too many arguments onlyl one needed";
        exit(0);
    }
    else
    {

    int n = (int)(*argv[1]);
    std::cout <<"f(f("<<n<<")) = " << f(f(n)) <<std::endl;

    }
}
