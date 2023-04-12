import sys
from heapq import heappush,heappop
input = sys.stdin.readline
V,E=map(int,input().split())
v,edges,q,answer,cnt=[0]*(V+1),[[] for _ in ' '*(V+1)],[[0,1]],0,0
for _ in ' '*E:
    s,e,w=map(int,input().split())
    edges[s].append((w,e))
    edges[e].append((w,s))
while q and cnt!=V:
    w,s=heappop(q)
    if not v[s]:
        v[s]=1
        answer+=w
        cnt+=1
        for edge in edges[s]:heappush(q,edge)
print(answer)