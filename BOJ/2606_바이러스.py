graph=[[] for _ in range(int(input())+1)]
visited,que = [],[1]
for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
while que:
    num = que.pop()
    if num in visited : continue
    visited.append(num)
    que+=graph[num]
print(len(visited)-1)