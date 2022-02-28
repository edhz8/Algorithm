import sys
input = sys.stdin.readline
N = int(input())
g = [list(input().strip().split()) for _ in range(N)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
X,Y,teachers=[],[],[]
for i in range(N):
    for j in range(N):
        if g[i][j] == 'T' : 
            X.append(i)
            Y.append(j)
            teachers.append((i,j))
points=[]
for x in range(N):
    for y in range(N):
        if (x in X or y in Y) and g[x][y] == 'X' : points.append((x,y))
L = len(points)
for i in range(L-2):
    ix,iy=points[i][0],points[i][1]
    g[ix][iy] = 'O'
    for j in range(i+1,L-1):
        jx,jy=points[j][0],points[j][1]
        g[jx][jy] = 'O'
        for k in range(j+1,L):
            kx,ky=points[k][0],points[k][1]
            g[kx][ky] = 'O'
            
            q = teachers[:]
            BREAK = False
            while q:
                x,y = q.pop(0)
                for dx,dy in D:
                    nx,ny = x,y
                    while True:
                        nx += dx
                        ny += dy
                        if not 0<=nx<N or not 0<=ny<N : break
                        if g[nx][ny] == 'S':
                            BREAK = True
                            break
                        elif g[nx][ny] == 'X' : continue
                        else : break
                    if BREAK : break
            if not BREAK :
                print('YES')
                exit(0)
            g[kx][ky] = 'X'
        g[jx][jy] = 'X'
    g[ix][iy] = 'X'
print('NO')