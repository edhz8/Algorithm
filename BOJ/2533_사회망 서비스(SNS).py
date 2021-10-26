import sys
sys.setrecursionlimit(10**9)
I = sys.stdin.readline
N = int(I())
graph,dp,visited = [[] for _ in range(N+1)],[[1,0] for _ in range(N+1)],[False for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,I().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += max(dp[child])
dfs(1)
print(N-max(dp[1]))