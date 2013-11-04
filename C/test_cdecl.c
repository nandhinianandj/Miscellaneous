int callee(int,int,int);

int caller(void)
{
    register int ret;

    ret = callee(1,2,3);
    ret += 5;
    return ret;
}
