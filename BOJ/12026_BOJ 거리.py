N,road,cur,nex=int(input()),input(),'B',{'B':'O','O':'J','J':'B'}
dp,dp[0] = [float('inf') for _ in range(N)],0
for i in range(N):
    # if dp[i] == float('inf') : continue
    cur = road[i]
    for j in range(i+1,N):
        if road[j] == nex[cur]: dp[j] = min(dp[j],dp[i]+pow(j-i,2))
print(dp[-1] if dp[-1]!=float('inf') else -1)