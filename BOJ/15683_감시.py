import sys
I = sys.stdin.readline
n,m=map(int,I().split())
graph=[list(map(int,I().split())) for _ in range(n)]
cctvs=[]
cctv={1:[(0),(1),(2),(3)] , 2:[(0,2),(1,3)] , 3:[(0,1),(1,2),(2,3),(3,4)] , 4:[(0,1,2),(1,2,3),(2,3,0),(3,1,2)] , 5:[(0,1,2,3)]}
D=((-1,0),(0,1),(1,0),(0,-1))
def get_nms(x,y,d):
    ret = []
    while True:
        x,y=x+D[d][0],y+D[d][1]
        if 0<=x<n and 0<=y<m:
            if graph[x][y] == 0 : ret.append((x,y))
            elif graph[x][y] == 6 : break
        else : break
    return ret
for x,y in [(i,j) for i in range(n) for j in range(m) if graph[i][j] in [1,2,3,4,5]]:
    tmp=[]
    for d in cctv[graph[x][y]]:
        t=[]
        for di in d:
            t+=get_nms(x,y,di)
        tmp.append(t)
    cctvs.append(tmp)

