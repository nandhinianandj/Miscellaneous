#include <stdlib.h>
#include <linux/random.h>

int main() {
    char * buf;
    int buflen;
    buflen = 1024;
    getrandom(buf, buflen);
}

