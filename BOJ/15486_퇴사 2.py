import sys
input = sys.stdin.readline
N=int(input())
dp=[0]*N
answer,prev=0,0
for i in range(N):
    t,p=map(int,input().split())
    prev=max(prev,dp[i-1] if i!=0 else 0)
    if i+t-1<N: 
        dp[i+t-1] = max(dp[i+t-1],prev + p)
        answer = max(answer,dp[i+t-1])
print(answer)
# 15486 10:53(35분소요)