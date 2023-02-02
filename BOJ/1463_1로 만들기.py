N=int(input())
dp,dp[1]=[float('inf')]*(N+1),0
for i in range(1,N):
    for j in [i+1,i*2,i*3]:
        if j<=N: dp[j] = min(dp[j],dp[i]+1)
        else : break
print(dp[N])