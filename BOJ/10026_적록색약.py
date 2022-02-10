import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
dx,dy = [-1,0,1,0],[0,1,0,-1];
            
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]
a1,a2=0,0

def dfs1(i,j):
    visited[i][j] = True
    for d in range(4):
        nx,ny = i+dx[d],j+dy[d]
        if 0<=nx<N and 0<=ny<N and graph[i][j]==graph[nx][ny] and not visited[nx][ny]:
            dfs1(nx,ny)
def dfs2(i,j):
    visited2[i][j] = True
    for d in range(4):
        nx,ny = i+dx[d],j+dy[d]
        if 0<=nx<N and 0<=ny<N and (graph[i][j]==graph[nx][ny] or (graph[i][j] in ['R','G'] and graph[nx][ny] in ['R','G'])) and not visited2[nx][ny]:
            dfs2(nx,ny)
            
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs1(i,j)
            a1+=1
        if not visited2[i][j]:
            dfs2(i,j)
            a2+=1
        
print(a1,a2)