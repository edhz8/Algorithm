import sys
input = sys.stdin.readline
N,M=map(int,input().split())
edges=sorted([[*map(int,input().split())] for _ in ' '*M],key=lambda x : x[2])
parent=[i for i in range(N+1)]
answer=0
def find_parent(x):
    if parent[x] != x : parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(x,y):
    x,y=find_parent(x),find_parent(y)
    if x<y : parent[y]=x
    else : parent[x]=y
prev=0
for x,y,w in edges:
    if find_parent(x) != find_parent(y) :
        union_parent(x,y)
        answer+=w
        prev=w
print(answer-prev)