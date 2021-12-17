import sys
import heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    if n:=int(input()): heapq.heappush(heap,n)
    elif heap : print(heapq.heappop(heap))
    else : print(0)