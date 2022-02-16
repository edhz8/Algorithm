import sys
input = sys.stdin.readline
N,ans=int(input()),0
g=[input().strip() for _ in range(N)]
for i in range(N):
    cnt=set()
    for j in range(N):
        if g[i][j]=='Y' :
            cnt.add(j)
            for k in range(N):
                if i!=k and g[j][k]=='Y' : cnt.add(k)
    ans = max(ans,len(cnt))
print(ans)