nums = [int(input()) for _ in  range(int(input()))]
M = max(nums)
dp,dp[1],dp[2],dp[3]=[0 for _ in range(M+1)],1,2,4
for i in  range(4,M+1): dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(*[dp[i] for i in nums],sep='\n')