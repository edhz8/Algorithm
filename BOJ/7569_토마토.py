import sys
from collections import deque
input = sys.stdin.readline
D=[(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
M,N,H=map(int,input().split())
G=[[[*map(int,input().split())] for _ in ' '*N]for _ in ' '*H]
q=deque([(h,n,m) for h in range(H)for n in range(N)for m in range(M)if G[h][n][m]==1])
answer = 0
while q:
    h,n,m=q.popleft()
    for dh,dn,dm in D:
        nh,nn,nm=h+dh,n+dn,m+dm
        if 0<=nh<H and 0<=nn<N and 0<=nm<M and G[nh][nn][nm]==0:
            G[nh][nn][nm]=G[h][n][m]+1
            q.append((nh,nn,nm))
for h in range(H):
    for n in range(N):
        for m in range(M):
            if G[h][n][m]==0: print(-1);exit(0)
            elif G[h][n][m]>0 : answer = max(answer,G[h][n][m])
print(answer-1)