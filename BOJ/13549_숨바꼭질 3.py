from heapq import heappush,heappop
N,K=map(int,input().split())
L=100000
dp,q=[float('inf')]*(L+1),[]
dp[N]=0
heappush(q,(0,N))
while q:
    time,index=heappop(q)
    if index==K:break
    for t,i in [(0,index*2),(1,index+1),(1,index-1)]:
        if not 0<=i<=L: continue
        if t+dp[index] < dp[i]:
            dp[i] = t+dp[index]
            heappush(q,(t+dp[index],i))
print(dp[K])
