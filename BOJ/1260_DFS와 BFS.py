import sys
from collections import deque

def dfs(v):
    print(v,end=' ')
    visited[v] = 1
    for i in range(1,N+1):
        if g[v][i] and not visited[i] : dfs(i)

def bfs(v):
    visited[v] = 1
    q=deque([v])
    while q:
        n = q.popleft()
        print(n,end=' ')
        for i in range(1,N+1):
            if g[n][i] and not visited[i] :
                q.append(i)
                visited[i] = 1

input = sys.stdin.readline
N,M,V=map(int,input().split())
g=[[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    g[x][y] = g[y][x] = 1
visited = [0 for _ in range(N+1)]
dfs(V)
print()
visited = [0 for _ in range(N+1)]
bfs(V)