#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "ex19.h"


int Monster_attack(void *self,int damage)
{
    Monster *monster = self;
    printf("You attack %s!\n",monster->_(description));
}
