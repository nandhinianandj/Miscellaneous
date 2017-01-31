#include <stdio.h>
#include <stdlib.h>

void fill(unsigned char* addr, size_t amount) {
    unsigned long i;
    for (i = 0; i < amount; i++) {
        *(addr + i) = 42;
    }
}

int main(int argc, char **argv) {

    unsigned char *result;
    char input;
    size_t s = 1<<30;

    result = malloc(s);
    printf("Addr: %p\n", result);
    //fill(result, s);

    scanf("%c", &input);
    return 0;
}
