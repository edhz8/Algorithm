from collections import defaultdict
import sys
input = sys.stdin.readline
N,M=map(int,input().split())
g=defaultdict(list)
for _ in range(N-1):
    a,b,d = map(int,input().split())
    g[a].append([b,d])
    g[b].append([a,d])
for _ in range(M):
    f,t=map(int,input().split())
    q = [(f,0)]
    visited = []
    while q:
        n,s = q.pop(0)
        if n==t : 
            print(s)
            break
        for cn,cs in g[n]:
            if cn in visited: continue
            visited.append(cn)
            q.append((cn,s+cs))