import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
D = [(-1,0),(0,1),(1,0),(0,-1)]
Max,cur,cnt=0,0,0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cnt,cur = cnt+1,1
            graph[i][j] = 2
            q = [(i,j)]
            while q:
                x,y=q.pop(0)
                for dx,dy in D:
                    nx,ny = x+dx,y+dy
                    if nx<0 or nx>=n or ny<0 or ny>=m or graph[nx][ny]!=1: continue
                    graph[nx][ny] = 2
                    cur +=1
                    q.append((nx,ny))
            Max = max(Max,cur)
print(cnt,Max,sep='\n')