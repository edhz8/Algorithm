import sys
input = sys.stdin.readline
n,l,r=map(int,input().split())
graph,time,D = [list(map(int,input().split())) for _ in range(n)],0,[(-1,0),(0,1),(1,0),(0,-1)]
def bfs(i,j):
    que,ret=[(i,j)],[(i,j)]
    while que:
        [i,j] = que.pop(0)
        for dx,dy in D:
            nx,ny=i+dx,j+dy
            if 0<=nx<n and 0<=ny<n and l<=abs(graph[i][j]-graph[nx][ny])<=r and (nx,ny) not in ret:
                que.append((nx,ny))
                ret.append((nx,ny))
    if len(ret)==1 : return False
    return ret
while True:
    total,groups=[],[]
    for i in range(n):
        for j in range(n):
            if (i,j) not in total:
                BFS = bfs(i,j)
                if BFS :
                    total+=BFS
                    groups.append(BFS)
    if not groups : print(time);break
    time+=1
    for group in groups:
        newNum = sum([graph[i][j] for i,j in group])//len(group)
        for i,j in group: graph[i][j] = newNum