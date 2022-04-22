from heapq import heappush,heappop
M,N=map(int,input().split())
g,q,dp=[list(map(int,list(input()))) for _ in range(N)],[],[[0 for _ in range(M)] for _ in range(N)]
D=[(-1,0),(0,1),(1,0),(0,-1)]
heappush(q,(0,0,0))
dp[0][0]=1
while q:
    wall,x,y=heappop(q)
    if x==N-1 and y==M-1 :
        print(wall)
        break
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and not dp[nx][ny]:
            dp[nx][ny] = 1
            heappush(q,(wall+g[nx][ny],nx,ny))