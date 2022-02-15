import sys
input = sys.stdin.readline
N,K=map(int,input().split())
dp=[0 for _ in range(N+1)]
for _ in range(K):
    I,T=map(int,input().split())
    for i in range(N,T-1,-1): dp[i] = max(dp[i],dp[i-T]+I)
print(dp)