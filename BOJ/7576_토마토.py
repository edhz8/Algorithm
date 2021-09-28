from collections import deque
import sys
I = sys.stdin.readline
m,n = map(int, I().split())
s,NOZERO = [],True
queue = deque()
D = ((-1,0),(0,1),(1,0),(0,-1))
for i in range(n):
    tmp = list(map(int, input().split()))
    if 0 in tmp : NOZERO = False
    s.append(tmp)
if NOZERO : print(0);exit(0)
def bfs():
    while queue:
        x,y = queue.popleft()
        for dx,dy in D:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
                s[nx][ny] = s[x][y] + 1
                queue.append((nx,ny))
for i in range(n):
    for j in range(m):
        if s[i][j] == 1: queue.append((i, j))
bfs()
NOZERO,Max = True,0
for i in range(n):
    if 0 in s[i] : NOZERO = False;break
    Max = max(Max,max(s[i]))
print(Max-1 if NOZERO else -1)