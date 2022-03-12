def solution(money, costs):
    dp,dp[0] = [float('inf') for i in range(money+1)],0
    for m,v in zip([1,5,10,50,100,500],costs):
        for i in range(money+1):
            if i+m > money : continue
            dp[i+m] = min(dp[i+m],dp[i]+v)
    return dp[money]