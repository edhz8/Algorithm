def solution(width, height, diagonals):
    ans = 0
    for a,b in diagonals:
        dp = [[0 for _ in range(width+1)] for _ in range(height+1)]
        for i in range(width+1):
            for j in range(height+1):
                if i==0 and j==0 : dp[i][j] =1 
                elif i == 0 : dp[i][j] = dp[i][j-1]
                elif j == 0 : dp[i][j] = dp[i-1][j]
                elif i==a and j==b