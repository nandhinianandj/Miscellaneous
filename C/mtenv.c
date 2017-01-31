#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

static void* worker(void* arg) {
  for (;;) {
    int i;
    char var[256], *p = var;

    for (i = 0; i < 8; ++i) {
      *p++ = 65 + (random() % 26);
    }

    *p++ = '\0';

    setenv(var, "test", 1);
  }

  return NULL;
}

int main() {
  pthread_t t;

  printf("start\n");
  setenv("foo", "bar", 0);
  pthread_create(&t, NULL, worker, 0);

  for (;;) {
    getenv("foo");
  }

  return 0;
}
