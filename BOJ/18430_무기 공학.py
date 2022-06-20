n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
shape = [[0,-1,1,0],[-1,0,0,-1],[-1,0,0,1],[0,1,1,0]]
visited = [[0] * m for _ in range(n)]
ans = 0
def dfs(X,Y,S) :
  global ans
  if Y == m : X += 1 ; Y = 0
  if X == n: ans = max(ans,S) ; return
  if not visited[X][Y] :
    for a,b,c,d in shape :
      x,y,z,w = X+a,Y+b,X+c,Y+d
      if 0<= x < n and 0 <= z < n and 0<= y < m and 0 <= w < m and not visited[x][y] and not visited[z][w] :
        visited[x][y] = visited[z][w] = visited[X][Y] = 1
        dfs(X,Y+1,S+board[X][Y]*2+board[x][y]+board[z][w])
        visited[X][Y] = visited[x][y] = visited[z][w] = 0
  dfs(X,Y+1,S)
dfs(0,0,0)
print(ans)