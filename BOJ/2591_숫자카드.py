s = input()
L,dp = len(s),[0 for _ in range(len(s))]
dp[0] = 1
dp[1] = (dp[0] if int(s[1])>0 else 0) + (9<int(s[:2])<35)
for i in range(2,L): dp[i] += (dp[i-1] if int(s[i])>0 else 0) + (dp[i-2] if 9<int(s[i-1:i+1])<35 else 0)
print(dp[-1])