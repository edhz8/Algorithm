import sys
input = sys.stdin.readline
N = int(input())
D = [(0,1),(-1,0),(0,-1),(1,0)] # 시계방향으로 가면 1씩 감소
answer = 0
v=[[0]*101 for _ in ' '*101]
for _ in range(N):
    x,y,d,g=map(int,input().split())
    x,y=y,x
    gen=0
    ds=[d]
    v[x][y]=1
    lx,ly=x+D[d][0],y+D[d][1]
    v[lx][ly]=1
    while gen<g:
        gen+=1
        tds = [*map(lambda x : x+1 if x<3 else 0 ,ds[::-1])]
        for d in tds:
            dx,dy=D[d]
            nx,ny=lx+dx,ly+dy
            v[nx][ny]=1
            lx,ly=nx,ny
        ds += tds
for i in range(100):
    for j in range(100):
        if v[i][j] and v[i+1][j] and v[i][j+1] and v[i+1][j+1] : answer +=1
print(answer)
