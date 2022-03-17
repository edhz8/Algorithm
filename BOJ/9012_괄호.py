for _ in range(int(input())):
    c,p=0,0
    for i in input():
        c += [-1,1][i=='(']
        if c<0 : p=1;break
    print('YNEOS'[p or c>0::2])