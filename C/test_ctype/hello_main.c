#include <stdio.h>
#include "hello.h"

struct helloStruct callback();

int main(int argc, char **argv) {
    float f;
    struct helloStruct result;
    printf ("Hello World\n");
    f = fxn(callback);
    printf("Callback result: %f\n",f);

}

struct helloStruct callback() {
    struct helloStruct result;
    result.i = 10;
    result.f = 3.14159;
    return result;
}

int int_callback() {
    return 42;
}


