N,M=map(int,input().split())
G=[[0]*(M+1)]+[[0,*map(int,input().split())] for _ in ' '*N]
for i in range(N+1):
    for j in range(M+1):G[i][j]+=(G[i-1][j]+G[i][j-1]-G[i-1][j-1])
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    print(G[c][d]-G[c][b-1]-G[a-1][d]+G[a-1][b-1])