n,*per = map(int,input().split())
D = [(0,1),(0,-1),(-1,0),(1,0)]
v = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
def dfs(x,y,p,cnt):
    if cnt==n: return p
    v[x][y] = 1
    ans = 0
    for d in range(4):
        dx,dy = D[d]
        nx,ny = x+dx,y+dy
        if v[nx][ny] or per[d]==0 : continue
        ans += dfs(nx,ny,p*per[d]/100,cnt+1)
        v[nx][ny] = 0
    return ans
print(dfs(n,n,1,0))