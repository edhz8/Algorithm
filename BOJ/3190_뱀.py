N,K=int(input()),int(input())
G=[[0]*N for _ in ' '*N]
D=[(-1,0),(0,1),(1,0),(0,-1)]
for _ in ' '*K :
    x,y=map(int,input().split())
    G[x-1][y-1]='a'
def turnL(cd): return cd-1 if cd>0 else 3
def turnR(cd): return cd+1 if cd<3 else 0
cd=1
turns = dict()
for _ in ' '*int(input()) :
    k,v=input().split()
    turns[int(k)]=v
ans=0
x,y=0,0
tx,ty=0,0
# print(turns)
while 1:
    ans+=1
    dx,dy=D[cd]
    nx,ny=x+dx,y+dy
    if (not 0<=nx<N) or (not 0<=ny<N) :break
    elif G[nx][ny]=='a' :
        # print('AA',x,y,nx,ny)
        G[x][y]=[nx,ny]
        x,y=nx,ny
    elif G[nx][ny] :break
    else :
        G[x][y] = [nx,ny]
        X,Y=tx,ty
        tx,ty = G[X][Y]
        G[X][Y] = 0
        x,y=nx,ny
    G[x][y] = 'H'
    print('-',ans,'(',x,y,')','D:',cd)
    if ans in turns : cd = turnL(cd) if turns[ans]=='L' else turnR(cd)
    for i in range(N) : print(*G[i])
print(ans)