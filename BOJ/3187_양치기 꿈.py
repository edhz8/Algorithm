import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
R,C = map(int,input().split())
g = [list(input().strip()) for _ in range(R)]
D,al,aw,lamb,wolf = [(-1,0),(0,1),(1,0),(0,-1)],0,0,0,0
def dfs(x,y):
    global lamb,wolf
    if g[x][y] == 'v' : wolf +=1
    elif g[x][y] == 'k' : lamb +=1
    g[x][y] = '#'
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if nx<0 or nx>=R or ny<0 or ny>=C or g[nx][ny]=='#': continue
        dfs(nx,ny)
for i in range(R):
    for j in range(C):
        if g[i][j] == '#' : continue
        lamb,wolf= 0,0
        dfs(i,j)
        if lamb > wolf : al += lamb
        else : aw += wolf
print(al,aw)