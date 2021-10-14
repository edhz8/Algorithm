for s in open(0):
    l,u,n,b=0,0,0,0
    for c in s: 
        l,u,n,b=l+int(c.islower()),u+int(c.isupper()),n+int(c.isnumeric()),b+int(c==' ')
    print(l,u,n,b)