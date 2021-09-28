import sys
I = sys.stdin.readline
n = int(I())
Map = [list(map(int,list(I().rstrip()))) for _ in range(n)]
D = ((-1,0),(0,1),(1,0),(0,-1))
ans = []
def dfs(i,j):
    Map[i][j] = 0
    ans[-1]+=1
    for dx,dy in D:
        nx,ny=i+dx,j+dy
        if 0<=nx<n and 0<=ny<n and Map[nx][ny]: dfs(nx,ny)
for i in range(n):
    for j in range(n):
        if Map[i][j] : ans.append(0);dfs(i,j)
print(len(ans),'\n'.join(map(str,sorted(ans))),sep='\n')