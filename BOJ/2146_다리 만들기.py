from collections import deque
n=int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
edges,count,D,length= deque(),2,[(-1,0),(0,1),(1,0),(0,-1)],0
def bfs(i,j):
    global count
    que = deque([(i,j)])
    while que:
        x,y = que.popleft()
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = count
                    que.append((nx,ny))
                elif graph[nx][ny] == 0 and (x,y,count) not in edges: 
                    graph[x][y] = count
                    edges.append((x,y,count))
    count += 1

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 : bfs(i,j)
while True:
    tedges = deque()
    while edges:
        x,y,z = edges.popleft()
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0 : 
                    tedges.append((nx,ny,z))
                    graph[nx][ny] = 1
                elif graph[nx][ny] > 1 and graph[nx][ny] != z : print(length);exit()
    edges,length = tedges,length+1