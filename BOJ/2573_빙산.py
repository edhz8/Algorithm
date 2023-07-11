N,M=map(int,input().split())
G=[[*map(int,input().split())]for _ in ' '*N]
D=[(-1,0),(0,1),(1,0),(0,-1)]
answer = 0
while 1:
    H=[G[n][:]for n in range(N)]
    cnt=0
    for x in range(N):
        for y in range(M):
            if H[x][y]==0 : continue
            cnt += 1
            if cnt>1: print(answer);exit(0)
            H[x][y]=0
            q=[(x,y)]
            while q:
                qx,qy=q.pop(0)
                for dx,dy in D:
                    nx,ny=qx+dx,qy+dy
                    if 0<=nx<N and 0<=ny<M and H[nx][ny]:
                        H[nx][ny]=0
                        q.append((nx,ny))
    if cnt == 0 : print(0);exit(0)
    H=[G[n][:]for n in range(N)]
    for x in range(N):
        for y in range(M):
            if H[x][y]==0: continue
            for dx,dy in D:
                nx,ny=x+dx,y+dy
                if 0<=nx<N and 0<=ny<M and H[nx][ny]==0 : G[x][y] -= 1
            G[x][y] = max(G[x][y],0)
    answer += 1