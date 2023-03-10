N=int(input())
G=[*map(int,input().split())]
dp=[1]*N
for i in range(N):
    for j in range(i):
        if G[j]>G[i] : dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))