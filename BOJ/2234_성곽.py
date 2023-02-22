import sys
input = sys.stdin.readline

N,M=map(int,input().split())
D=[(1,0),(0,1),(-1,0),(0,-1)] #남동북서
G=[[*map(lambda x : bin(int(x))[2:].zfill(4),input().split())] for _ in 'M'*M]
answer = [0,0,0]
def dfs(x,y):
    global v,cur,room_set
    v[x][y]=answer[0]
    for d in range(4):
        dx,dy=D[d]
        nx,ny=x+dx,y+dy
        if G[x][y][d]=='1' :
            if 0<=nx<M and 0<=ny<N and v[nx][ny] and v[nx][ny] != answer[0]: room_set.add(v[nx][ny])
            continue 
        if 0<=nx<M and 0<=ny<N and not v[nx][ny]: 
            dfs(nx,ny)
            cur+=1
room_info=[]    
room_size=[0]
v=[[0]*N for _ in ' '*M]
for x in range(M):
    for y in range(N):
        if not v[x][y] : 
            answer[0]+=1
            cur=1
            room_set=set()
            dfs(x,y)
            room_info.append(room_set)
            room_size.append(cur)
            answer[1]=max(answer[1],cur)
for i in range(len(room_info)):
    for j in room_info[i]:
        answer[2] = max(answer[2],room_size[i+1]+room_size[j])
print(*answer,sep='\n')