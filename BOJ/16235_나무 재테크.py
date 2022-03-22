N,M,K=map(int,input().split())
winter,age = [list(map(int,input().split())) for _ in range(N)],[[[] for _ in range(N)] for _ in range(N)]
g,year = [[5 for _ in range(N)] for _ in range(N)],0
for _ in range(M):
    x,y,z = map(int,input().split())
    age[x-1][y-1].append(z)
for i in range(N):
    for j in range(N):
        if age[i][j] : age[i][j].sort()
while year<K:
    fall = []
    for i in range(N):
        for j in range(N):
            if not age[i][j] : continue
            summer,nage = 0,[]
            while age[i][j]:
                p = age[i][j].pop(0)
                if g[i][j] >= p :
                    g[i][j] -= p
                    nage.append(p+1)
                    if (p+1) %5==0 : fall.append((i,j))
                else : summer+=(p//2)
            age[i][j] = nage
            g[i][j] += summer
            
    for x,y in fall:
        for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]: 
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N : age[nx][ny].insert(0,1)
    
    for x in range(N):
        for y in range(N):
            g[x][y] += winter[x][y]
            
    year += 1
print(sum([len(age[i][j]) for i in range(N) for j in range(N)]))