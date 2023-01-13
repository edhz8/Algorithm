from collections import defaultdict,deque
n=int(input())
x,y=map(int,input().split())
G=defaultdict(list)
v=[0]*(n+1)
for _ in range(int(input())):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
q=deque([(x,0)])
while q:
    f,n=q.popleft()
    if f==y: print(n);exit(0)
    for node in G[f]: 
        if not v[node] :q.append((node,n+1));v[node]=1
print(-1)
# 10:14(14분 소요)