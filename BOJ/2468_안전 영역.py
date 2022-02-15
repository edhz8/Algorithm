import sys
sys.setrecursionlimit(10**5)
I = sys.stdin.readline
n = int(I())
graph,heights,D,vlist=[],set(),((-1,0),(0,1),(1,0),(0,-1)),[[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    t=list(map(int,I().split()))
    heights.update(t)
    graph.append(t)
def dfs(h,x,y):
    vlist[x][y]=1
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not vlist[nx][ny] and graph[nx][ny]> h: dfs(h,nx,ny)
def search(h):
    global vlist
    ret = 0
    vlist = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not vlist[i][j] and graph[i][j]>h:
                ret+=1
                dfs(h,i,j)
    return ret
print(max([search(h) for h in heights]+[1]))