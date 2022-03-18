import sys
I = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,I().split())
g,dp = [list(map(int,I().split())) for _ in range(n)],[[-1 for _ in range(m)] for _ in range(n)]
def dfs(x,y):
    if x==n-1 and y==m-1 : return 1
    if dp[x][y] > -1 : return dp[x][y]
    dp[x][y] = 0
    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and  g[nx][ny] < g[x][y]: dp[x][y] += dfs(nx,ny)
    return dp[x][y]
print(dfs(0,0))