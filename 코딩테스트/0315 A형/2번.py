g,v,ans,C = 0,0,float('inf'),0
def dfs(c,l):
    global ans
    END = True
    for i in range(-C,C+1):
        if (i<0 and not v[i] and v[-i]) or (i>0 and not v[i]) :
            END = False
            v[i] = 1
            dfs(i,l+g[c][i])
            v[i] = 0
    if END : ans = min(ans,l)  
for T in range(1,int(input())+1):
    ans,N,xy,C = float('inf'),int(input()),[(0,0) for _ in range(10)],0
    for i in range(N):
        for j,n in enumerate(map(int,input().split())):
            if n==0 : continue
            C = max(C,n)
            xy[n] = (i,j)
    g,v = [[0 for _ in range((C+1)*2)] for _ in range((C+1)*2)],[0 for _ in range((C+1)*2)]
    for i in range(-C,C+1):
        for j in range(-C,C+1): g[i][j] = (abs(xy[i][0]-xy[j][0]) + abs(xy[i][1]-xy[j][1]))
    dfs(0,0)
    print('#',T,' ',ans,sep='')