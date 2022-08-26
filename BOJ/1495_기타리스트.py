N,S,M = map(int,input().split())
V=list(map(int,input().split()))
dp,dp[0][S]=[[0]*(M+1) for _ in ' '*(N+1)],1
for i in range(N):
    for j in range(M+1):
        if dp[i][j] : 
            if j-V[i]>=0 : dp[i+1][j-V[i]] = 1
            if j+V[i]<=M : dp[i+1][j+V[i]] = 1
for i in range(M,-1,-1):
    if dp[N][i] : print(i);exit(0)
print(-1)
