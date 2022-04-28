import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
D = [(-1,0),(0,1),(1,0),(0,-1)]
N,M=map(int,input().split())
g = [list(map(int,input().split())) for _ in range(N)]
def dfs(x,y):
    v[x][y] = -1
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<M :
            if g[nx][ny] == 0 and v[nx][ny]==0: dfs(nx,ny)
            elif g[nx][ny] == 1 : v[nx][ny] += 1
sec = 0
while 1:
    v = [[0 for _ in range(M)] for _ in range(N)]
    dfs(0,0)
    END = True
    for i in range(N):
        for j in range(M):
            if g[i][j] == 1 : END = False
            if v[i][j]>1 : g[i][j] = 0
    if END : break
    sec += 1
print(sec)