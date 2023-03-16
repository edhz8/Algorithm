N=int(input())
n=1
answer=0
yuks=[]
dp=[0]*(N+1)
while 2*n*n-n <= N : yuks.append(2*n*n-n);n+=1
for yuk in yuks : dp[yuk]=1
for i in range(1,N+1):
    cur=7
    for yuk in yuks:
        index=i-yuk
        if index<0 : break
        cur=min(cur,dp[index])
    dp[i]=cur+1
print(dp[-1])