import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
cnt,ans = 0,[]
for _ in range(M):
    a,b=map(int,input().split())
    graph[b].append(a)
for i in range(1,N+1):
    q,cur,visited = deque([i]),1,[0 for _ in range(N+1)]
    visited[i] = 1
    while q:
        num = q.popleft()
        for j in graph[num]:
            if not visited[j]:
                cur+=1
                q.append(j)
                visited[j]=1
    if cnt<cur : cnt,ans = cur,[i]
    elif cnt==cur : ans.append(i)
print(*ans)