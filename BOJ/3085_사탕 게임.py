import sys
input = sys.stdin.readline
N=int(input())
G=[list(input()) for _ in ' '*N]
D=[(-1,0),(0,1),(1,0),(0,-1)]
answer=0
for x in range(N):
    for y in range(N):
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                G[x][y],G[nx][ny]=G[nx][ny],G[x][y]
                t=0
                while y-t>=0 and G[x][y]==G[x][y-t]: t+=1
                b=0
                while y+b<N and G[x][y]==G[x][y+b]: b+=1
                l=0
                while x-l>=0 and G[x][y]==G[x-l][y]: l+=1
                r=0
                while x+r<N and G[x][y]==G[x+r][y]: r+=1
                G[x][y],G[nx][ny]=G[nx][ny],G[x][y]
                answer = max(answer,t+b-1,l+r-1)
print(answer)