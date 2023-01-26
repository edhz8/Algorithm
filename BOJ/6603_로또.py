from itertools import combinations
while 1:
    k,*s = map(int,input().split())
    if k == 0 : break
    for c in combinations(s,6): print(*c)
    print()
# 10:11