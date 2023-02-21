import sys
input = sys.stdin.readline
N,M=map(int,input().split())
G=[[*map(int,input().split())] for _ in ' '*N]
D=[(0,-1),(1,0),(0,1),(-1,0)] #북동남서
cctv={
    1:[[0],[1],[2],[3]],
    2:[(0,2),(1,3)],
    3:[(0,1),(1,2),(2,3),(3,0)],
    4:[(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
    5:[(0,1,2,3)]
}
points=[]
answer = N*M
for x in range(N):
    for y in range(M):
        if G[x][y]>0: answer-=1 
        if 0<G[x][y]<6:
            ps = []
            for dx,dy in D:
                nx,ny=x+dx,y+dy
                t=set()
                while 0<=nx<N and 0<=ny<M and 0<=G[nx][ny]<6:
                    if G[nx][ny]==0 : t.add((nx,ny))
                    nx+=dx
                    ny+=dy
                ps.append(t)
            nps = []
            for ways in cctv[G[x][y]]:
                t=set()
                for way in ways: t|=ps[way]
                nps.append(t)
            points.append(nps)
L=len(points)
Max=0
def rec(index,S):
    global Max
    if index==L:
        Max = max(Max,len(S));return
    for s in points[index]: rec(index+1,S|s)
rec(0,set())
print(answer-Max)
