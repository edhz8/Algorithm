import sys
input = sys.stdin.readline
K = int(input())
W,H = map(int,input().split())
v = [[[float('inf'),float('inf')] for _ in range(W)] for _ in range(H)] # (총 움직임,말 움직임) 
g = [list(map(int,input().split())) for _ in range(H)]
q = [(0,0)]
v[0][0] = [0,0]
HD = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
while q:
    x,y = q.pop(0)
    if v[x][y][1]<K :
        for hx,hy in HD:
            nx,ny = x+hx,y+hy
            if -1<nx<H and -1<ny<W and g[nx][ny]==0 and v[nx][ny][0]>=(v[x][y][0]+1):
                v[nx][ny][0],v[nx][ny][1] = v[x][y][0]+1,min(v[nx][ny][1],v[x][y][1]+1)
                if nx==W-1 and ny == H-1 : 
                    print(v[nx][ny][0])
                    exit(0)
                else : q.append((nx,ny))
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if -1<nx<H and -1<ny<W and g[nx][ny]==0 and v[nx][ny][0]>=(v[x][y][0]+1):
            v[nx][ny][0],v[nx][ny][1] = v[x][y][0]+1,min(v[nx][ny][1],v[x][y][1])
            if nx==W-1 and ny == H-1 : 
                print(v[nx][ny][0])
                exit(0)
            else : q.append((nx,ny))
print(-1)