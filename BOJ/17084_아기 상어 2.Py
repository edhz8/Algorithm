import sys
input = sys.stdin.readline
N,M=map(int,input().split())
G=[list(map(int,input().split())) for _ in ' '*N]
q=[(i,j) for i in range(N) for j in range(M) if G[i][j]]
D=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
MAX=0
while q:
    x,y=q.pop(0)
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and not G[nx][ny]:
            G[nx][ny] = G[x][y]+1
            MAX=max(MAX,G[nx][ny])
            q.append((nx,ny))
print(MAX-1)