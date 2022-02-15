from heapq import heapify,heappop,heappush
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
q=list(map(int,input().split()))
heapify(q)
for _ in range(m):
    s = heappop(q)+heappop(q)
    heappush(q,s)
    heappush(q,s)
print(sum(q))