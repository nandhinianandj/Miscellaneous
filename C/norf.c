int main(void)
{
   int i;
   char *p = (char *)0x10000;
   for (i = 0; i < 1000000;i++) 
   {
      *p++ = 0;
   }

   for (i=0;i<1000000;i++)
   {;}

   return 0;
}
