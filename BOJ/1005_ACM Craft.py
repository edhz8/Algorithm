import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    N,K=map(int,input().split())
    building=[0]+list(map(int,input().split()))
    tree,inDegree,dp=[[] for _ in range(N+1)],[0 for _ in range(N+1)],[0 for _ in range(N+1)]
    for _ in range(K):
        a,b=map(int,input().split())
        tree[a].append(b)
        inDegree[b]+=1
    que = deque()
    for i in range(1,N+1):
        if inDegree[i]==0:
            que.append(i)
            dp[i]=building[i]
    while que:
        a=que.popleft()
        for i in tree[a]:
            inDegree[i]-=1
            dp[i]=max(dp[a]+building[i],dp[i])
            if inDegree[i]==0: que.append(i)
    print(dp[int(input())])