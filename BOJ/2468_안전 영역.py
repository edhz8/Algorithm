import sys
I = sys.stdin.readline
n = int(I())
graph,heights,Max,D,vlist=[],set(),-1,((-1,0),(0,1),(1,0),(0,-1)),[]
for _ in range(n):
    t=list(map(int,I().split()))
    heights.update(t)
    graph.append(t)
def dfs(h,x,y):
    global vlist
    vlist.append((x,y))
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if ((nx,ny) not in vlist) and 0<=nx<n and 0<=ny<n and graph[nx][ny]> h: dfs(h,nx,ny)
def search(h):
    global vlist
    ret = 0
    vlist = []
    for i in range(n):
        for j in range(n):
            if ((i,j) not in vlist) and graph[i][j]>h:ret+=1;dfs(h,i,j)
    return ret
for h in list(heights): Max = max(Max,search(h))
print(Max)