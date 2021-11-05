r,c=map(int,input().split())
graph = [list(input()) for _ in range(r)]
D,res = [(-1,0),(0,1),(1,0),(0,-1)],0
que = set([(graph[0][0],0,0)])
while que:
    [visited,x,y] = que.pop()
    for dx,dy in D:
        nx,ny = x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in visited : 
            que.add((visited+graph[nx][ny],nx,ny))
        else : res = max(res,len(visited))
print(res)