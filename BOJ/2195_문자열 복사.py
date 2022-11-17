from collections import defaultdict
from heapq import heappop,heappush
S,P=input(),input()
q=[]
v={(0,0)}
heappush(q,(0,0))
starts = defaultdict(list)
for i,s in enumerate(S) : starts[s].append(i)
while q:
    si,cnt=heappop(q)
    si=-si
    if si>=len(P) : print(cnt);exit(0)
    for start in starts[P[si]]:
        length=0
        while start+length<len(S) and si+length<len(P) and S[start+length]==P[si+length]: length+=1
        if (-(si+length),cnt+1) not in v : 
            heappush(q,(-(si+length),cnt+1))
            v.add((-(si+length),cnt+1))