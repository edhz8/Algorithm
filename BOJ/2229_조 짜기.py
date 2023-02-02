N=int(input())
arr = [*map(int,input().split())]
dp = [0]*(N+1)
for i in range(N):
    Max = Min = arr[i]
    for j in range(i,-1,-1):
        Max = max(Max,arr[j])
        Min = min(Min,arr[j])
        dp[i+1]=max(dp[i+1],dp[j]+Max-Min)
print(dp[N])