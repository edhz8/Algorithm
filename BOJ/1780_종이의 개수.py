import sys
input = sys.stdin.readline
N=int(input())
G=[[*map(int,input().split())] for _ in ' '*N]
answer = [0]*3
def rec(x,y,l):
    num = G[x][y]
    if all([num==G[i][j] for i in range(x,x+l) for j in range(y,y+l)]): answer[num+1]+=1
    else:
        nl=l//3
        rec(x,y,nl)
        rec(x+nl,y,nl)
        rec(x+nl*2,y,nl)
        rec(x,y+nl,nl)
        rec(x,y+nl*2,nl)
        rec(x+nl,y+nl,nl)
        rec(x+nl*2,y+nl,nl)
        rec(x+nl,y+nl*2,nl)
        rec(x+nl*2,y+nl*2,nl)
rec(0,0,N)
print(*answer)