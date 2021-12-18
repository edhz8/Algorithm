import heapq
import sys
I,h = sys.stdin.readline,[]
for _ in range(int(I())):
    if n:=int(I()): heapq.heappush(h,-n)
    elif h: print(-heapq.heappop(h))
    else : print(0)