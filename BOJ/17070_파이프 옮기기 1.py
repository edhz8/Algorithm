N=int(input())
G=[[*map(int,input().split())] for _ in ' '*N]
answer=0
dp=[[[0,0,0] for _ in ' '*N] for _ in ' '*N]#[가로,세로,대각]
dp[0][1][0]=1
for x in range(N):
    for y in range(N):
        if G[x][y]==1 : continue
        cur=sum(dp[x][y])
        bx,by=x+1,y
        if bx<N and by<N and G[bx][by]==0: dp[bx][by][1] += (cur-dp[x][y][0])
        bx,by=x,y+1
        if bx<N and by<N and G[bx][by]==0: dp[bx][by][0] += (cur-dp[x][y][1])
        bx,by=x+1,y+1
        if bx<N and by<N and G[bx-1][by]==0 and G[bx][by-1]==0 and G[bx][by]==0:dp[bx][by][2] += cur
print(sum(dp[-1][-1]))