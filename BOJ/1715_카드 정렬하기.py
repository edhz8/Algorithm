import sys
from heapq import heappush,heappop
input,deck,ret = sys.stdin.readline,[],0
for _ in range(int(input())): heappush(deck,int(input()))
while len(deck)>1:
    tmp = (heappop(deck) + heappop(deck))
    ret += tmp
    heappush(deck,tmp)
print(ret)