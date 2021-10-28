S=input()
L=len(S)
dp,dp[1],dp[2]=[0 for _ in range(L+1)],1,(1 if int(S[:2]) > 34 else 2)
for i in range(3,L+1):
    dp[i] = (dp[i-1] if int(S[i-1]) > 0 else 0) + (dp[i-2] if 10 <= int(S[i-2:i]) <= 34 else 0)
print(dp[-1])