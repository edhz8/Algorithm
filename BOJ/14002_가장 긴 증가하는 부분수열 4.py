import sys
input = sys.stdin.readline
N,arr = int(input()),list(map(int, input().split()))
dp,ans = [1]*N,[]

for i in range(1, N):
    for j in range(i):
        if arr[i]>arr[j]: dp[i] = max(dp[i], dp[j]+1)

order = max(dp)
print(order)
for i in range(N-1, -1, -1):
    if dp[i]==order:
        ans.append(arr[i])
        order-=1
print(*ans[::-1])