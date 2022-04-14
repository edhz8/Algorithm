from heapq import heappush,heappop
n,D=int(input()),[(-1,0),(0,1),(1,0),(0,-1)]
g,v,q=[list(map(int,input())) for _ in range(n)],[[0 for _ in range(n)]for _ in range(n)],[]
heappush(q,[0,0,0])
v[0][0] = 1
while q:
    c,x,y=heappop(q)
    if x==n-1 and y==n-1 : print(c)
    for dx,dy in D:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not v[nx][ny]: 
            v[nx][ny] = 1
            heappush(q,[c+(g[nx][ny]^1),nx,ny])