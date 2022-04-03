C,N = map(int,input().split())
dp,dp[0] = [float('inf') for _ in range(C+100)],0
for _ in range(N):
    v,w=map(int,input().split())
    for i in range(w,C+100): dp[i] = min(dp[i],dp[i-w]+v)
print(min(dp[C:]))