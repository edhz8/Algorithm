from collections import defaultdict
from heapq import heappush,heappop
def solution(genres, plays):
    d,infos=defaultdict(int),defaultdict(list)
    for i,[g,p] in enumerate(zip(genres,plays)):
        d[g]-=p
        heappush(infos[g],[-p,i])
    return [heappop(infos[g])[1] for g,n in sorted(d.items(),key=lambda x:x[1]) for _ in range(2) if infos[g]]