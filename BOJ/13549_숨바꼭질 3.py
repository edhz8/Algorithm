from heapq import heappop,heappush
N,K=map(int,input().split())
q=[]
L = 100001
dp,dp[N] = [float('inf') for _ in range(L)],0
heappush(q,(0,N))
while q:
    time,index = heappop(q)
    for node in[(0,index*2),(1,index+1),(1,index-1)]:
        if node[1] <0 or node[1]>=L : continue
        if node[0]+dp[index] < dp[node[1]]:
            dp[node[1]] = node[0]+dp[index]
            heappush(q,node)
print(dp[K])