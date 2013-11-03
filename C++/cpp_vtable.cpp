#include <iostream>

struct X
{
    int a;
    char b;
    int c;
    virtual void set_value(int v) {a = v; }
    virtual int get_value(int v) {return a; }
    virtual void increase_value() { a++;}


};

struct Y
{
    int a;
    char b;
    int c;
    virtual void set_value(int v) {a = v;}

};

int main(void)
{
    std:: cout << sizeof(X) << std::endl;
    std:: cout << sizeof(Y) << std::endl;
    return 1;

}

