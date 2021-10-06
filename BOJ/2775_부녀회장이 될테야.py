I = lambda : int(input())
for _ in range(I()):
    a,b=I(),I()
    dp=[[i for i in range(b+1)] for _ in range(a+1)]
    for i in range(1,a+1):
        for j in range(1,b+1):
            dp[i][j] = sum(dp[i-1][:j+1])
    print(dp[a][b])