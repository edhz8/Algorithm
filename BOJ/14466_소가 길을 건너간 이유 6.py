import sys
from collections import defaultdict
input = sys.stdin.readline
D=[(-1,0),(0,1),(1,0),(0,-1)]
N,K,R=map(int,input().split())
answer = K*(K-1)//2
roads = defaultdict(list)
Int = lambda x: int(x)-1
for _ in range(R):
    a,b,c,d=map(Int,input().split())
    roads[(a,b)].append((c,d))
    roads[(c,d)].append((a,b))
print(roads)
G=[[0]*N for _ in ' '*N]
for i in range(K):
    x,y=map(Int,input().split())
    G[x][y] = i+1
def dfs(x,y):
    global G,cnt
    G[x][y]=-1
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<N and (nx,ny) not in roads[(x,y)] and G[nx][ny]>-1:
            if G[nx][ny] : cnt+=1
            dfs(nx,ny) 

for i in range(N):
    for j in range(N):
        if G[i][j]>0:
            cnt=1
            dfs(i,j)
            answer -= cnt*(cnt-1)//2
print(answer)