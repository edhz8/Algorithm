import sys
input = sys.stdin.readline
N=int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
g[0].append(1)
q=list(map(int,input().split()))
def dfs(index):
    if not q : print(1);exit(0)
    while q[0] in g[index] : dfs(q.pop(0))
dfs(0)