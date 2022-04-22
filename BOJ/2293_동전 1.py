n,k=map(int,input().split())
dp=[1]+[0 for _ in range(1,k+1)]
for _ in ' '*n:
    c = int(input())
    for i in range(c,k+1): dp[i]+=dp[i-c]
print(dp[k])