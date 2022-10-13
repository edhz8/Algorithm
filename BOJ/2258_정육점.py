import sys
input = sys.stdin.readline
N,M=map(int,input().split())
meats = sorted([list(map(int,input().split())) for _ in ' '*N])
SUM=0
cweight,cnt,ccost=0,0,float('inf')
for i,[weight,cost] in enumerate(meats):
    if weight==0: continue
    if cweight<weight : 
        SUM += cweight * cnt
        if ccost<=cost and SUM>=M : print(ccost);exit(0)
        cweight,cnt,ccost = weight,1,cost
    elif cweight == weight : 
        cnt += 1
        ccost += cost
    if i==N-1 : SUM += cweight * cnt
    if SUM>=M : print(ccost);exit(0)
print(-1)