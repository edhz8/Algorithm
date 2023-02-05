import sys
input = sys.stdin.readline
K,N=map(int,input().split())
ks=[int(input()) for _ in ' '*K]
s,e = 1,max(ks)
while s<=e:
    m = (s+e)//2
    if sum(k//m for k in ks)>=N : s=m+1
    else: e=m-1
print(e)