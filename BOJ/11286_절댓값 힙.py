import heapq
import sys
I = sys.stdin.readline
heap = []
for _ in range(int(I())):
    if n:=int(I()) : heapq.heappush(heap,(abs(n),n))
    elif heap : print(heapq.heappop(heap)[1])
    else : print(0)