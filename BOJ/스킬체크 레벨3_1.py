def solution(n):
    if n==1 : return 1
    dp,dp[0],dp[1]=[0 for _ in range(n)],1,2
    for i in range(2,n): dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]%1234567