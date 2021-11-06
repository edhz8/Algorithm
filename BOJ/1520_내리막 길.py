import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
graph,dp = [list(map(int,input().split())) for _ in range(n)],[[-1 for _ in range(m)] for _ in range(n)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
def dfs(x,y):
    if x==n-1 and y==m-1 : return 1
    if dp[x][y] != -1 : return dp[x][y]
    dp[x][y] = 0
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and  graph[nx][ny] < graph[x][y]: dp[x][y] += dfs(nx,ny)
    return dp[x][y]
print(dfs(0,0))