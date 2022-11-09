def solution(triangle):
    L=len(triangle)
    dp = [0]*L
    for line in triangle:
        for i in range(len(line)-1,-1,-1):
            dp[i] = line[i] + max((dp[i-1] if 0<=i-1 else 0),dp[i])
    return max(dp)