def solution(abilities, k):
    abils = sorted(abilities)
    L = len(abilities)//2
    dp = [[0 for _ in range(k+1)] for _ in range(L + 1)]
    for i in range(L):
        bg,sm = abils.pop(),abils.pop()
        if i==0 : dp[0][0],dp[0][1] =sm,bg ; continue
        for j in range(k+1): dp[i][j] = max(dp[i-1][j]+sm , dp[i-1][j-1]+bg) if j else dp[i-1][j]+sm
    for i in range(k+1): dp[L][i] = dp[L-1][i-1] + abils.pop() if i and abils else dp[L-1][i]
    return max(dp[L])