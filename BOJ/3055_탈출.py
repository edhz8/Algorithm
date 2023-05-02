from collections import deque
R,C=map(int,input().split())
G=[list(input()) for _ in ' '*R]
sx,sy=0,0
for i in range(R):
    for j in range(C):
        if G[i][j]=='S' : sx,sy=i,j;G[i][j]='.'
D=[(-1,0),(0,1),(1,0),(0,-1)]
v=set()
def inRange(x,y) : return 0<=x<R and 0<=y<C
def answer(ans) :
    print(ans)
    exit(0)
def water():
    global G
    new=set()
    for x in range(R):
        for y in range(C):
            if G[x][y]=='*' and (x,y) not in new:
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if inRange(nx,ny) and G[nx][ny]=='.' :
                        G[nx][ny]='*'
                        new.add((nx,ny))
q=deque([(sx,sy)])
v.add((sx,sy))
sec=0
while 1:
    nextq=deque()
    sec+=1
    water()
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if inRange(nx,ny) and G[nx][ny] not in ['*','X'] and (nx,ny) not in v:
                v.add((nx,ny))
                if G[nx][ny]=='D' : answer(sec) 
                nextq.append((nx,ny))
    if not nextq:answer('KAKTUS')
    else : q=nextq