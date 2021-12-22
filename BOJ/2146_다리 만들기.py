from collections import deque
n=int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
edges = []
visited = []
D = [(-1,0),(0,1),(1,0),(0,-1)]
def bfs(i,j):
    cntEdges = []
    que = deque([(i,j)])
    while que:
        x,y = que.popleft()
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] and (nx,ny) not in visited:
                    visited.append((nx,ny))
                    que.append((nx,ny))
                elif graph[nx][ny] == 0 and (x,y) not in cntEdges: cntEdges.append((x,y))
    edges.append(cntEdges)


for i in range(n):
    for j in range(n):
        if graph[i][j] and (i,j)not in visited : bfs(i,j)

