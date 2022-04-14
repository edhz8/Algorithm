n = int(input())
if n%2==1 : print(0);exit()
dp,dp[2] = [0 for i in range(n+1)],3
for i in range(4,n+1,2):
    dp[i]=3*dp[i-2]+2
    for j in range(4,i,2): dp[i]+=2*dp[i-j]
print(dp[n])