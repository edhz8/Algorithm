n=int(input())
stars=[[*map(float,input().split())] for _ in ' '*n]
edges=sorted([[((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2)**0.5,i,j] for i in range(n) for j in range(i+1,n)])
parent=[i for i in range(n+1)]
answer=0
def find_parent(x):
    if parent[x]!=x:parent[x]=find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a,b = find_parent(a),find_parent(b)
    if a<b: parent[b]=a
    else : parent[a]=b
for w,x,y in edges:
    if find_parent(x) != find_parent(y) :
        union_parent(x,y)
        answer += w
print(round(answer,2))