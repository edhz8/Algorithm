from copy import deepcopy
from itertools import combinations
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
zeros = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 : zeros.append((i,j))
combis = list(combinations(zeros,3))
D=((-1,0),(0,1),(1,0),(0,-1))
queue = deque()
def bfs(craph):
    while queue:
        x,y=queue.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m  and craph[nx][ny]==0 : 
                craph[nx][ny]=2
                queue.append((nx,ny))
    ret = 0
    for i in range(n):
        for j in range(m): 
            if craph[i][j] == 0 : ret+=1
    return ret
def getCount(walls):
    craph=deepcopy(graph)
    for i,j in walls: craph[i][j] = 1
    for i in range(n):
        for j in range(m):
            if craph[i][j] == 2 : queue.append((i,j))
    return bfs(craph)
ans = 0
for com in combis: ans = max(ans,getCount(com))
print(ans)