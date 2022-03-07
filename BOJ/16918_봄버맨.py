import sys
input = sys.stdin.readline
r,c,N = map(int,input().split())
mp,bomb,D = [list(input().strip()) for _ in range(r)],[],[(-1,0),(0,1),(1,0),(0,-1),(0,0)]
for n in range(2,N+1):
    if n%2==0 : 
        for x in range(r):
            for y in range(c):
                if mp[x][y]=='O' : bomb.append((x,y))
                else : mp[x][y]='O'
    else :
        for x,y in bomb:
            for dx,dy in D:
                nx,ny=x+dx,y+dy
                if -1<nx<r and -1<ny<c: mp[nx][ny] = '.'
        bomb =  []
for i in range(r): print(*mp[i],sep='')