nums,NA = [int(input()) for _ in range(int(input()))],1000000009
N = max(nums)
dp,dp[1][0],dp[2][1],dp[3] = [[0 for _ in range(3)] for _ in range(N+1)],1,1,[1,1,1]
for i in range(4,N+1): dp[i][0],dp[i][1],dp[i][2] = (dp[i-1][1]+dp[i-1][2])%NA,(dp[i-2][0]+dp[i-2][2])%NA,(dp[i-3][0]+dp[i-3][1])%NA
print(*[sum(dp[i])%NA for i in nums])