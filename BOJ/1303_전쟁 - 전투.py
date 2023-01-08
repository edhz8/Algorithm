from collections import deque
N,M=map(int,input().split())
G=[list(input()) for _ in ' '*M]
D=[(-1,0),(0,1),(1,0),(0,-1)]
def bfs(i,j):
    global G
    c=G[i][j]
    G[i][j]=0
    q=deque([(i,j)])
    ret = 1
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and G[nx][ny]==c:
                G[nx][ny] = 0
                q.append((nx,ny))
                ret+=1
    return ret*ret
white,blue=0,0
for i in range(M):
    for j in range(N):
        if G[i][j] == 0 : continue
        if G[i][j] == 'W' : white += bfs(i,j)
        if G[i][j] == 'B' : blue += bfs(i,j)
print(white,blue)
# 1303 10:18(11분소요)