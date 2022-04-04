N = int(input())
g,dp=[int(input()) for _ in range(N)],[0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if g[i]<g[j] : dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))