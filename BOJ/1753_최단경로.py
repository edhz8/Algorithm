import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 100000000
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dp[k] = 0
heappush(heap, [0, k])
while heap:
    w, n = heappop(heap)
    for node, weight in graph[n]:
        new_weight = weight + w
        if new_weight < dp[node]:
            dp[node] = new_weight
            heappush(heap, [new_weight, node])
print(*[i if i != inf else "INF" for i in dp[1:]],sep='\n')