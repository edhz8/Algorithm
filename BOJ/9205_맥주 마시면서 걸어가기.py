v,n,pp,rx,ry,h,dp=0,0,0,0,0,0,0
def dfs(cur):
    global v,n,pp,rx,ry,h
    if h: return
    for p in range(n):
        if not v[p] and dp[cur][p] <=1000 :
            v[p] = 1
            dfs(p)
    if dp[cur][n+1] <=1000 : h=1;return
for _ in range(int(input())):
    n = int(input())
    sx,sy = map(int,input().split())
    pp = [tuple(map(int,input().split())) for _ in range(n)] + [(sx,sy),tuple(map(int,input().split()))]
    v,h,dp = [0 for _ in range(n)],0,[[abs(pp[i][0]-pp[j][0]) + abs(pp[i][1]-pp[j][1]) for i in range(n+2)] for j in range(n+2)]
    dfs(n)
    print(['sad','happy'][h])