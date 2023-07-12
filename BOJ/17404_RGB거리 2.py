N=int(input())
answer = float('inf')
G=[[*map(int,input().split())]for _ in' '*N]
for i in range(3):
    dp=[float('inf')]*3
    dp[i]=G[0][i]
    for j in range(1,N): dp=[G[j][0]+min(dp[1],dp[2]),G[j][1]+min(dp[0],dp[2]),G[j][2]+min(dp[0],dp[1])]
    for j in range(3):
        if i!=j : answer = min(answer, dp[j])
print(answer)