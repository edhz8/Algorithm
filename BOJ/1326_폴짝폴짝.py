from collections import deque
N=int(input())
arr=[*map(int,input().split())]
a,b=map(int,input().split())
v=[0]*N
a-=1
b-=1
q=deque([(a,0)])
while q:
    i,cnt=q.popleft()
    if i==b:
        print(cnt)
        exit(0)
    dist=0
    while 0<=i+dist+arr[i]<N:
        dist+=arr[i]
        if not v[i+dist]:
            v[i+dist]=1
            q.append((i+dist,cnt+1))
    dist=0
    while 0<=i-(dist+arr[i])<N:
        dist+=arr[i]
        if not v[i-dist]:
            v[i-dist]=1
            q.append((i-dist,cnt+1))
print(-1)
# 1226