import sys
input = sys.stdin.readline
N,M=map(int,input().split())
g=[list(map(int,input().split())) for _ in ' '*N]
D=[(0,-1),(1,0),(0,1),(-1,0)]
MAX = 0
def dfs(x,y,cur,SUM):
    global v,MAX
    if cur == 4 :MAX = max(MAX,SUM);return
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and not v[nx][ny]:
            v[nx][ny]=1
            dfs(nx,ny,cur+1,SUM+g[nx][ny])
            v[nx][ny]=0
def fu(x,y):
    global MAX
    w=[(x-1,y),(x,y+1),(x+1,y),(x,y-1)]*2
    for i in range(4):
        flag,s=1,g[x][y]
        for tx,ty in w[i:i+3]:
            if 0<=tx<N and 0<=ty<M: s += g[tx][ty]
            else : flag=0;break
        if flag : MAX = max(MAX,s)

for i in range(N):
    for j in range(M):
        v=[[0]*M for _ in ' '*N]
        dfs(i,j,1,0)
        fu(i,j)
print(MAX)