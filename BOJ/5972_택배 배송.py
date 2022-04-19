from heapq import heappop,heappush
from collections import defaultdict
N,M=map(int,input().split())
g,v,q=defaultdict(list),[float('inf') for _ in range(N+1)],[]
heappush(q,(0,1))
v[1] = 0
for _ in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
while q:
    yeo,hut = heappop(q)
    if hut == N : 
        print(yeo)
        break
    for K,V in g[hut]:
        if v[K]>yeo+V:
            v[K] = yeo+V
            heappush(q,(yeo+V,K))