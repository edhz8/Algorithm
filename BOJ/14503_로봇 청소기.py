import sys
I = sys.stdin.readline
n,m = map(int,I().split())
x,y,d = map(int,I().split())
mp = [list(map(int,I().split())) for _ in range(n)]
dx,dy,rev,mp[x][y],ans,end=(-1,0,1,0),(0,1,0,-1),(2,3,0,1),2,1,0
while True:
    d = d-1 if d else 3
    tx,ty = x+dx[d],y+dy[d]
    target = mp[tx][ty]
    if target == 0 : x,y,mp[tx][ty],end,ans = tx,ty,2,0,ans+1
    else : 
        end+=1
        if end==4 :
            bx,by = x+dx[rev[d]],y+dy[rev[d]]
            back = mp[bx][by]
            if back == 1 : break
            elif back == 2 :  x,y,end = bx,by,0
print(ans)