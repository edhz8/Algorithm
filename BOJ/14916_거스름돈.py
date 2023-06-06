n=int(input())
F=1e9
dp=[0,F,1,F,2,1]
for i in range(n-5):dp+=[min(dp[-2],dp[-5])+1]
print([-1,dp[n]][dp[n]<F])