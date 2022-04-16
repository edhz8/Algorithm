from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(N)]
H,W,X,Y,fx,fy = map(int,input().split())
fx-=1
fy-=1
D = [(-1,0),(0,1),(1,0),(0,-1)]
q = deque([(X-1,Y-1,0)])
while q:
    x,y,cnt = q.popleft()
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        YES = True
        if g[nx][ny] > 0 : continue
        for i in range(nx,nx+H):
            for j in range(ny,ny+W):
                if 0<=i<N and 0<=j<M :
                    if g[i][j]==1 : YES = False;break
                else : YES = False ;break
            if not YES : break
        if YES :
            if nx==fx and ny==fy : print(cnt+1);exit()
            else : 
                g[nx][ny] = 2
                q.append((nx,ny,cnt+1))
print(-1)