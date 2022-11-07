A,B=map(int,input().split())
N,M=map(int,input().split())
G=[[0 for _ in ' '*A] for _ in ' '*B]
D=[(-1,0),(0,1),(1,0),(0,-1)]
xy=[0]*(N+1)
for i in range(N):
    y,x,d=input().split()
    X,Y=B-int(x),int(y)-1
    G[X][Y] = [i+1,{'N':0,'E':1,'S':2,'W':3}[d]]
    xy[i+1] = (X,Y)
for i in range(M):
    bot,cmd,num=input().split()
    bot,num=map(int,[bot,num])
    for j in range(num):
        x,y=xy[bot]
        d=G[x][y][1]
        if cmd=='L' : G[x][y] = [bot,3 if d==0 else d-1]
        if cmd=='R' : G[x][y] = [bot,0 if d==3 else d+1]
        if cmd=='F' : 
            dx,dy=D[d]
            nx,ny=x+dx,y+dy
            if (not 0<=nx<B) or (not 0<=ny<A) : print('Robot',bot,'crashes into the wall');exit(0)
            if G[nx][ny] : print('Robot',bot,'crashes into robot',G[nx][ny][0]);exit(0)
            G[nx][ny] = G[x][y]
            xy[bot] = (nx,ny)
            G[x][y] = 0
print('OK')