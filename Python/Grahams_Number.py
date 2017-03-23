def GrahamsNumber():
    # This may take awhile...
    g = 4
    for n in range(1,64+1):
        g = hyperop(g+2)(3,3)
    return g
