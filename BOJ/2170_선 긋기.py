import sys
input = sys.stdin.readline
N = int(input())
xys = sorted([tuple(map(int,input().split())) for _ in range(N)])
X=Y=-float('inf')
ans=0
for x,y in xys:
    if Y<x :
        ans += (y-x)
        X,Y=x,y
    elif Y<y:
        ans += (y-Y)
        Y = y
print(ans)