import itertools
N,M = map(int,input().split())
for i in sorted(set(itertools.permutations(map(int,input().split()),M))): print(*i)