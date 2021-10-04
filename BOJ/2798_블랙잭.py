from itertools import combinations
m=int(input().split()[1]);print(max([sum(s) for s in combinations(list(map(int,input().split())),3) if sum(s)<=m]))