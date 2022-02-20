from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
W,H = map(int,input().split())
graph = [[0 for _ in range(W)] for _ in range(H)]
D,X,Y = [(-1,0),(0,1),(1,0),(0,-1)],0,0
R = [[0,1,3],[1,0,2],[2,1,3],[3,0,2],[0,1,2,3]]
FOUND = False
for i in range(H):
    IS=input().strip()
    for j in range(W):
        graph[i][j] = IS[j]
        if not FOUND and IS[j] == 'C' : X,Y,graph[i][j],FOUND = i,j,0,True
PRT = float('inf')
q=deque([[X,Y,-1]])
while q:
    x,y,d = q.popleft()
    for i in R[d]:
        [dx,dy] = D[i]
        nx,ny = x+dx,y+dy
        nans = graph[x][y]+(0 if d==-1 or d%2==i%2 else 1)
        if nx<0 or nx>=H or ny<0 or ny>=W or graph[nx][ny] == '*' or (graph[nx][ny] not in ['.','S','C'] and graph[nx][ny] < nans) or nans>PRT : continue
        if graph[nx][ny] == 'C' : 
            PRT = min(PRT,nans)
            continue
        graph[nx][ny] = nans
        q.append([nx,ny,i])
print(PRT)