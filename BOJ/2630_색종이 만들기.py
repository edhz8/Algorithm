import sys
input = sys.stdin.readline
N = int(input())
g = [list(map(int,input().split())) for _ in range(N)]
ZERO,ONE=0,0
def rec(x,y,n):
    global ZERO,ONE
    c = g[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if c==g[i][j] : continue
            h=n//2
            rec(x,y,h)
            rec(x+h,y,h)
            rec(x,y+h,h)
            rec(x+h,y+h,h)
            return
    if c==0 : ZERO +=1
    else : ONE +=1
rec(0,0,N)
print(ZERO,ONE,sep='\n')