from collections import deque
import sys
input = sys.stdin.readline
R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
ans = 0
D = [(-1,0),(0,1),(1,0),(0,-1)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'L':
            visited = [[0 for _ in range(C)] for _ in range(R)]
            visited[i][j] = 1
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                for dx,dy in D:
                    nx,ny = x+dx,y+dy
                    if nx<0 or nx>=R or ny<0 or ny>=C or graph[nx][ny]=='W' or visited[nx][ny]: continue
                    visited[nx][ny] = visited[x][y] + 1
                    ans = max(ans,visited[nx][ny])
                    q.append((nx,ny))
print(ans-1)