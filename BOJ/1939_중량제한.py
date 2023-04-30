import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
G=[[] for _ in ' '*(N+1)]
for _ in ' '*M:
    A,B,C=map(int,input().split())
    G[A].append((B,C))
    G[B].append((A,C))
start,end=map(int,input().split())
def bfs(weight):
    v=[0]*(N+1)
    q=deque([start])
    v[start]=1
    while q:
        cur=q.popleft()
        if cur==end : return True
        for to,w in G[cur]:
            if not v[to] and weight<=w : v[to]=1;q.append(to) 
    return False
lo,hi,answer=1,1000000000,0
while lo<=hi:
    mid=(lo+hi)//2
    if bfs(mid): answer=mid;lo=mid+1
    else : hi=mid-1
print(answer)