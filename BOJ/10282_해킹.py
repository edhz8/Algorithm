import sys
from heapq import heappop,heappush
input = sys.stdin.readline
for _ in range(int(input())):
    n,d,c=map(int,input().split())
    g=[[] for _ in range(n+1)]
    dp = [float('inf') for _ in range(n+1)]
    v = [0 for _ in range(n+1)]
    for _ in range(d):
        a,b,w=map(int,input().split())
        g[b].append([a,w])
    q=[]
    dp[c] = 0
    heappush(q,(0,c))
    while q:
        wei,no=heappop(q)
        if v[no] : continue
        v[no] = True
        for node,weight in g[no]:
            nw = wei+weight
            if nw<dp[node]:
                dp[node] = nw
                heappush(q,(nw,node))
    a,b=0,0
    for num in dp:
        if num!=float('inf') : 
            a+=1
            b=max(b,num)
    print(a,b)