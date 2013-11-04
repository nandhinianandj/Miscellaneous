#include <stdio.h>
#include "hello.h"

float fxn (struct helloStruct callback()) {

    struct helloStruct result = callback();

    printf("i: %d\n",result.i);
    printf("f: %f\n",result.f);
    return result.f * result.i;
}


