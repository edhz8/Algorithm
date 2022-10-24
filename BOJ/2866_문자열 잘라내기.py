import sys
from collections import defaultdict
input = sys.stdin.readline
R,C=map(int,input().split())
S=[input() for _ in ' '*R]
q=[list(range(C))]
ans=0
for i,s in enumerate(S[::-1]):
    if not q: ans=R-i;break
    tq=[]
    while q:
        d = defaultdict(list)
        for j in q.pop(): d[s[j]].append(j)
        tq+=[l for l in d.values() if len(l)>1]
    q=tq
print(ans)