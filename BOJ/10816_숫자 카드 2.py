from collections import defaultdict
d=defaultdict(int)
input()
for n in input().split(): d[n] += 1
input();print(*[d[n] for n in input().split()])