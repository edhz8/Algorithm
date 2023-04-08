import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
G=[[] for _ in ' '*(N+1)]
nums=[0]*(N+1)
q=deque()
for _ in ' '*M:
    t,b=map(int,input().split())
    G[t].append(b)
    nums[b]+=1
for i in range(1,N+1):
    if nums[i]==0 : q.append(i)
answer=[]
while q:
    cur = q.popleft()
    answer.append(cur)
    for b in G[cur]:
        nums[b]-=1
        if nums[b]==0 : q.append(b)
print(*answer)