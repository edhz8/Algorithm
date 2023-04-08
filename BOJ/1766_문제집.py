import sys
from heapq import heappop,heappush
input = sys.stdin.readline
N,M=map(int,input().split())
level=[0]*(N+1)
tos=[[] for _ in range(N+1)]
for _ in range(M):
    f,t=map(int,input().split())
    tos[f].append(t)
    level[t]+=1
q=[]
for i in range(1,N+1):
    if level[i]==0 : heappush(q,i)
answer = []
while q:
    cur = heappop(q)
    answer.append(cur)
    for to in tos[cur] :
        level[to]-=1
        if level[to]==0 : heappush(q,to)
print(*answer)
