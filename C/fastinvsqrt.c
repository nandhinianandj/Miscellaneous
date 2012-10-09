#include<stdio.h>
#include<time.h>
float FastInvSqrt(float x){
  float xhalf = 0.5f * x;
  int i = *(int*)&x; // hmm address of x typecast to an integer pointer and then the pointer dereferenced. Hmm why??
  i = 0x5f3759df - (i >> 1); //Magic address - i right shifted by one bit(or divide by 2)

  x = *(float*)&i; // same thing as i assignment above,but this is float
 
  x = x*(1.5f - (xhalf*x*x)); // this is just newton's approximation method one step
  return x;
}

void main()
{
  mt_bestseed();
  int r = rand()%100;
  printf("random number %d \n",r);
  printf("And it's inverse root%f\n",FastInvSqrt(r));
}
