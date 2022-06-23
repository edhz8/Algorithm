from heapq import heappush,heappop
import sys
input = sys.stdin.readline
plus,minus,ans,MAX=[],[],0,0
N,M=map(int,input().split())
for n in map(int,input().split()):
    if n>0 : heappush(plus,-n)
    else : heappush(minus,n)
def cal(heap):
    global ans,MAX
    while heap:
        cur = abs(heappop(heap))
        for _ in range(M-1):
            if not heap : break
            heappop(heap)
        MAX = max(MAX,cur)
        ans+=2*cur
cal(plus)
cal(minus)
ans -= MAX
print(ans)