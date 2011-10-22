#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

int main(int argc, char **argv)
{
  void *handle;
  double (*cosine)(double);
  char *error;

  handle = dlopen("libm.so",RTLD_LAZY);
  if (!handle) {
    fprintf(stderr,"%s\n", dlerror());
    exit(EXIT_FAILURE);
  }

  dlerror();


