from heapq import heappush,heappop
N,M,X,*L=map(int,open(0).read().split())
G=[[] for _ in ' '*(N+1)]
for f,t,v in L:G[f]+=[(t,v)]
def D(S,E):
    q,d=[(0,S)],[10**6]*(N+1)
    while q:
        V,C=heappop(q)
        if C==E:return V
        for c,v in G[C]:
            if V+v<d[c]:d[c]=V+v;heappush(q,(V+v,c))
print(max(D(i,X)+D(X,i)for i in range(1,N+1)))