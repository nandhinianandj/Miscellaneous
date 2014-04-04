# 1 "extern.c"
# 1 "<command-line>"
# 1 "extern.c"
int x=42;
int func1() {
    int x = 3840;
    {
        extern int x;
        printf("%d\n",x);
        return x;
    }
}
int func() {
    int x = 3840;
    {
        return x;
    }
}

void main(void)
{
    func1();
    printf("%d\n",func());
}
