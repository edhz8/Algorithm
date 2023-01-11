G=[[0]*101 for _ in ' '*101]
ix,iy=0,0
answer=100000
def dfs(x,y,cnt):
    global G,answer,ix,iy
    D=[(-1,0),(0,1),(1,0),(0,-1)]
    # print(x,y,'cnt=',cnt)
    if x==ix and y==iy : answer = min(answer,cnt);return
    else : G[x][y]=0
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<101 and 0<=ny<101 and G[nx][ny]: dfs(nx,ny,cnt+1)
def solution(rectangle, characterX, characterY, itemX, itemY):
    global G,cx,cy,answer,ix,iy
    ix,iy,characterX,characterY=itemX*2,itemY*2,characterX*2,characterY*2
    rectangle = [*map(lambda c:[c[0]*2,c[1]*2,c[2]*2,c[3]*2],rectangle)]
    for lx,ly,rx,ry in rectangle:
        for x in range(lx,rx+1):
            for y in range(ly,ry+1):G[x][y]=1
    for lx,ly,rx,ry in rectangle:
        for x in range(lx+1,rx):
            for y in range(ly+1,ry):G[x][y]=0
    # for i in range(30) : print(*G[i][:30])
    dfs(characterX,characterY,0)
    return answer//2