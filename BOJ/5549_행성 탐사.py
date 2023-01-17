import sys
input = sys.stdin.readline
M,N = map(int,input().split())
K=int(input())
G=[input() for _ in ' '*M]
dp=[[[0,0,0] for _ in ' '*N] for _ in ' '*M]
I={'J':0,'O':1,'I':2}
for i in range(M):
    for j in range(N):
        for k in range(3):
            dp[i][j][k] = (dp[i-1][j][k] if i>0 else 0) + (dp[i][j-1][k] if j>0 else 0) - (dp[i-1][j-1][k] if i>0 and j>0 else 0)
        dp[i][j][I[G[i][j]]]+=1
for _ in ' '*K:
    a,b,c,d=map(lambda x:int(x)-1,input().split())
    a-=1
    b-=1
    print(*[dp[c][d][i]-(dp[a][d][i] if a>=0 else 0)-(dp[c][b][i] if b>=0 else 0)+(dp[a][b][i] if a>=0 and b>=0 else 0) for i in range(3)])