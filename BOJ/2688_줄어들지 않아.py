import sys
input = sys.stdin.readline
ts = [int(input()) for _ in range(int(input()))]
n=max(ts)
dp=[[1 for _ in range(10)] for _ in range(n+1)]
for x in range(1,n+1):
    for y in range(9,-1,-1):
        dp[x][y] = dp[x-1][y] + (dp[x][y+1] if y<9 else 0)
for t in ts: print(dp[t][0])