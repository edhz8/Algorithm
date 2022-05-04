import sys
input = sys.stdin.readline
N=int(input())
g = [[] for _ in range(N+1)]
v = [0 for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
g[0].append(1)
q=list(map(int,input().split()))
def dfs(index):
    if len(q)==1 : print(1);exit(0)
    if q and q[0] in g[index] : 
        v[q[0]] = 1
        dfs(q.pop(0))
    for i in g[index]:
        if not v[i] : dfs(i)
dfs(0)
print(0)
print(q)