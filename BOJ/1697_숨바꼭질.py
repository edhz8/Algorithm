from collections import deque
def bfs(v):
    count = 0
    q = deque([[v, count]])
    while q:
        e,count = q.popleft()
        if not visited[e]:
            visited[e] = True
            if e == k: return count
            count += 1
            if (e * 2) <= 100000: q.append([e * 2, count])
            if (e + 1) <= 100000: q.append([e + 1, count])
            if (e - 1) >= 0: q.append([e - 1, count])
    return count       
n,k = map(int, input().split())
visited = [False] * 100001
print(bfs(n))