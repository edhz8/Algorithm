import sys
input = sys.stdin.readline
n,m=map(int,input().split())
time,prev,graph=0,0,[]
D=[(-1,0),(0,1),(1,0),(0,-1)]
for i in range(n):
    line = list(map(int,input().split()))
    prev+=line.count(1)
    graph.append(line)
def findNotHole():
    ret,que=[(0,0)],[(0,0)]
    while que:
        [i,j]=que.pop(0)
        for dx,dy in D:
            nx,ny=i+dx,j+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 1 and (nx,ny) not in ret: 
                que.append((nx,ny))
                ret.append((nx,ny))
    return ret
while True:
    NOT_HOLE=findNotHole()
    time,gone=time+1,[]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 1 : continue
            C=False
            for dx,dy in D:
                nx,ny=i+dx,j+dy
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and (nx,ny) in NOT_HOLE: C=True;break
            if C: gone.append((i,j))
    for i,j in gone: graph[i][j] = time+1
    if prev == len(gone): print(time,prev,sep='\n');break
    prev-=len(gone)