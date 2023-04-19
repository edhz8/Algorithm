import sys
from bisect import bisect_left
input = sys.stdin.readline
ks,vs=[],[]
N,M=map(int,input().split())
for _ in range(N):
    k,v=input().split()
    ks.append(k)
    vs.append(int(v))
for _ in range(M): print(ks[bisect_left(vs,int(input()))])