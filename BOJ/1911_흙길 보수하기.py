import sys
from math import ceil
input = sys.stdin.readline
N,L= map(int,input().split())
nuls = sorted([tuple(map(int,input().split())) for _ in range(N)])
print(nuls)
last = nuls[0][0]-1
ans = 0
for s,e in nuls:
    last = max(s,last)
    cnt = ceil((e-last)/L)
    last += L*cnt
    ans += cnt
print(ans)