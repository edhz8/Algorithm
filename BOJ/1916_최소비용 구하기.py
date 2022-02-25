import sys
from heapq import heappop,heappush
input = sys.stdin.readline
N,M = int(input()),int(input())
g = [[] for _ in range(N+1)]
dp = [float('inf') for _ in range(N+1)]
v = [0 for _ in range(N+1)]
for _ in range(M):
    a,b,w=map(int,input().split())
    g[a].append([b,w])
f,t=map(int,input().split())
q=[]
dp[f] = 0
heappush(q,(0,f))
while q:
    w,n=heappop(q)
    if v[n] : continue
    v[n] = True
    for node,weight in g[n]:
        nw = weight + w
        if nw<dp[node]:
            dp[node] = nw
            heappush(q,(nw,node))
print(dp[t])