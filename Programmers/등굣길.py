def solution(m, n, puddles):
    dp=[[0 for _ in ' '*m] for _ in ' '*n]
    dp[0][0]=1
    for x,y in puddles : dp[y-1][x-1]=-1
    for i in range(n):
        for j in range(m):
            if (i==0 and j==0) or dp[i][j]==-1: continue
            dp[i][j] = (dp[i-1][j] if i!=0 and dp[i-1][j]!=-1 else 0) + (dp[i][j-1] if j!=0and dp[i][j-1]!=-1 else 0)
            dp[i][j]%=1000000007
    return dp[-1][-1]