import sys
input = sys.stdin.readline
n,m=map(int,input().split())
P=[i for i in range(n)]
def find(x):
    if P[x]!=x:P[x]=find(P[x])
    return P[x]
def union(x,y):
    x,y=find(x),find(y)
    if x==y : return True
    if x<y : P[y]=x
    else : P[x]=y
    return False
for i in range(1,m+1):
    if union(*map(int,input().split())) : print(i);exit(0)
print(0)
