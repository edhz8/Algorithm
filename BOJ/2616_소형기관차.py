N=int(input())
nums=[*map(int,input().split())]
L=int(input())
prefix,prefix[L-1]=[0]*N,sum(nums[:L])
for i in range(L,N): prefix[i]=prefix[i-1]-nums[i-L]+nums[i]
dp=[[0]*N for _ in range(3)]
for i in range(N) : dp[0][i] = max(prefix[i],dp[0][i-1] if i>0 else 0)
for step in range(1,3):
    for i in range(N) : 
        if i-L>=0 and dp[step-1][i-L]: dp[step][i] = max(dp[step-1][i-L] + prefix[i],dp[step][i-1] if i>0 else 0)
print(dp[-1][-1])