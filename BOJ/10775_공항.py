import sys
input = sys.stdin.readline
G,P=int(input()),int(input())
parent=[i for i in range(G+1)]
answer=0
def find(x):
    if parent[x]!=x : parent[x]=find(parent[x])
    return parent[x]
for i in range(P):
    x=find(int(input()))
    if x==0 : answer=i;break
    y=find(x-1)
    parent[x]=y
print(answer if answer else P)