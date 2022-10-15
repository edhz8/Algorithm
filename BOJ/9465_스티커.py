for _ in ' '*int(input()):
    n=int(input())
    dp=[list(map(int,input().split())) for _ in 'dp']

    if n==1 : print(max(dp[0][0],dp[1][0]));continue
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-2],dp[1][i-1])
        dp[1][i] += max(dp[0][i-2],dp[0][i-1])
    print(max(dp[0][-1],dp[1][-1]))
