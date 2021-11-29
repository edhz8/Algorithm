n=int(input())
if n<3 : print(n)
else :
    dp,dp[1],dp[2] = [0 for _ in range(n+1)],1,2
    for i in range(3,n+1) : dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%10007)