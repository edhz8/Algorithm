import sys
input = sys.stdin.readline
T,W=map(int,input().split())
jadus=[int(input()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T)]
dp[0][0] = 1 if jadus[0] ==1 else 0
dp[0][1] = 0 if jadus[0] ==1 else 1
for t in range(1,T):
    for w in range(min(t+2,W+1)):
        jadu = int(w%2+1==jadus[t])
        dp[t][w] = (max(dp[t-1][w],dp[t-1][w-1]) if w>0 else dp[t-1][w])+jadu
print(max(dp[-1]))