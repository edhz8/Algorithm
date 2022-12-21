def solution(n, money):
    dp = [1]+[0]*n
    for m in money:
        for i in range(n):
            if i+m>n:break
            dp[i+m]+=dp[i]
    return dp[-1]%1000000007