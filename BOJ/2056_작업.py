import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
G,nums,time=[[] for _ in ' '*(N+1)],[0]*(N+1),[0]*(N+1)
for i in range(1,N+1):
    t,cnt,*gs=map(int,input().split())
    time[i]=t
    nums[i]=cnt
    for g in gs: G[g].append(i)
q=deque()
for i in range(1,N+1):
    if nums[i]==0 : q.append(i)
answer=0
prev=[0]*(N+1)
while q:
    cur = q.popleft()
    answer = max(answer,prev[cur]+time[cur])
    for g in G[cur]:
        nums[g] -= 1
        prev[g] = max(prev[g],prev[cur]+time[cur])
        if nums[g] == 0 : q.append(g)
print(answer)