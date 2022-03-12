import sys
from itertools import combinations
sys.setrecursionlimit(10**7)
N,g,visited,ans = 0,0,0,set()
def dfs(start,x,cnt):
    global ans
    NOT_VISITED = True
    for i in range(N):
        if i==start : continue
        if g[x][i] and i not in visited: 
            NOT_VISITED = False
            visited.append(i)
            dfs(start,i,cnt+1)
            visited.pop()
    if NOT_VISITED and len(visited)>1 : 
        for a,b in combinations(visited,2):
            t = tuple(sorted((start,a,b)))
            ans.add(t)
    
def solution(n, edges):
    global N,g,visited
    N,g = n,[[0 for _ in range(n)] for _ in range(n)]
    for x,y in edges: g[x][y] = g[y][x] = 1
    for i in range(n): 
        visited = []
        dfs(i,i,0)
    return len(ans)*2