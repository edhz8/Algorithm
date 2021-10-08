import sys
I = sys.stdin.readline
sys.setrecursionlimit(10**5)
LOG = 21

n=int(I())
parent,d,c = [[0 for _ in range(LOG)] for _ in range(n+1)],[0 for _ in range(n+1)],[0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,I().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    c[x],d[x] = True,depth
    for y in graph[x]:
        if c[y] : continue
        parent[y][0] = x
        dfs(y,depth+1)

def set_parent():
    dfs(1,0)
    for i in range(1,LOG):
        for j in range(1,n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
            
def lca(a,b):
    if d[a] > d[b] : a,b=b,a
    
    for i in range(LOG-1,-1,-1):
        if d[b] - d[a] >= (1<<i): b=parent[b][i]
        
    if a==b : return a
    
    for i in range(LOG - 1,-1,-1):
        if parent[a][i] != parent[b][i]: a,b=parent[a][i],parent[b][i]
    
    return parent[a][0]

set_parent()

for i in range(int(I())): print(lca(*map(int,I().split())))