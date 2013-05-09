int x=42;
int func() {
    int x = 3840;
    {
        extern int x;
        printf("%d",x);
        return x;
    }
}

