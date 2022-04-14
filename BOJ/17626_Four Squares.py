n = int(input())
dp = [i for i in range(n+1)]
for i in range(2,int(n**0.5)+1):
    num = i**2
    for j in range(n+1):
        if num+j > n : break
        dp[num+j] = min(dp[num+j],dp[j]+1)
print(dp[n])