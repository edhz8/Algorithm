import sys
input = sys.stdin.readline
N,D = map(int,input().split())
dp = [i for i in range(D+1)]
js = []
for _ in range(N):
    a,b,v = map(int,input().split())
    if a<D and b<=D : js.append((b,a,v))
js.sort()
for b,a,v in js: 
    dp[b] = min(dp[b],dp[a]+v)
    for i in range(b+1,D+1): dp[i] = dp[b] + (i-b)
ans = dp[D]
for i in range(1,D) : ans = min(ans,dp[i]+(D-i))
print(ans)