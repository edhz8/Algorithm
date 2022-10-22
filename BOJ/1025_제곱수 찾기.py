R,C=map(int,input().split())
G=[input() for _ in ' '*R]
def F(r,c,y,x):
    V,X,Y,M = 0,c,r,-1
    while 0<=X<C and 0<=Y<R and not (x==0 and y==0): V,X,Y=10*V+int(G[Y][X]),X+x,Y+y;M=max(M,-1 if (V**0.5)%1 else V)
    return M
print(max([F(r,c,y,x) for r in range(R) for c in range(C) for y in range(-r,R-r+1) for x in range(-c,C-c+1)]))