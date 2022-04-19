import sys
sys.setrecursionlimit(10**5)
M,N,K=map(int,input().split())
g=[[0 for _ in range(M)] for _ in range(N)]
D,areas,area,cnt=[(-1,0),(0,1),(1,0),(0,-1)],[],0,0
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2): g[i][j] = 1
def dfs(x,y):
    global area
    g[x][y]=1
    area+=1
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and g[nx][ny] == 0 : dfs(nx,ny)
        
for i in range(N):
    for j in range(M):
        if g[i][j] : continue
        area=0
        cnt+=1
        dfs(i,j)
        areas.append(area)
print(cnt)
print(*sorted(areas))