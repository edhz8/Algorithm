R,C,K=map(int,input().split())
g,D,ans=[[+(i=='T') for i in input()] for _ in ' '*R],[(-1,0),(0,1),(1,0),(0,-1)],0
def rec(x,y,k):
    global ans
    if k<2 :
        ans+=(x==0 and y==C-1)
        return
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<R and 0<=ny<C and g[nx][ny]==0:
            g[nx][ny]=1
            rec(nx,ny,k-1)
            g[nx][ny]=0
g[R-1][0]=1
rec(R-1,0,K)
print(ans)