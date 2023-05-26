import heapq as h
L=lambda:map(int,input().split())
N,M,X=L()
G=[[]for _ in' '*(N+1)]
for _ in' '*M:f,*a=L();G[f]+=[a]
def D(S,E):
    q,d=[(0,S)],[2e9]*(N+1)
    while q:
        V,C=h.heappop(q)
        if C==E:return V
        for c,v in G[C]:
            if V+v<d[c]:d[c]=V+v;h.heappush(q,(V+v,c))
print(max(D(i,X)+D(X,i)for i in range(1,N+1)))