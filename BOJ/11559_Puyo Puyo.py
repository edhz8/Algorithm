D=[(-1,0),(0,1),(1,0),(0,-1)]
G = [list(input()) for _ in ' '*12]
flag = True
answer = 0
def dfs(x,y,char):
    global v,cnt,points
    v[x][y]=1
    cnt+=1
    points.append((x,y))
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<12 and 0<=ny<6 and G[nx][ny]==char and not v[nx][ny]: dfs(nx,ny,char)
while flag:
    v=[[0]*6 for _ in ' '*12]
    flag=False
    for x in range(12):
        for y in range(6):
            if G[x][y]=='.' or v[x][y] : continue
            cnt=0
            points=[]
            dfs(x,y,G[x][y])
            if cnt>=4 : 
                flag=True
                for px,py in points : G[px][py]='.'
    for x in range(10,-1,-1):
        for y in range(6):
            tx=x+1
            char = G[x][y]
            while tx<12:
                if G[tx][y]=='.':
                    G[tx][y]=char
                    G[tx-1][y]='.'
                    tx+=1
                else : break
    if flag : answer+=1
print(answer)