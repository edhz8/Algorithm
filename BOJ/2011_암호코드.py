S,MOD=input(),1000000
L = len(S)
dp,dp[0] = [0 for _ in range(L)],int(S[0]!='0')
for i in range(1,L):
    if int(S[i])>0 : dp[i] += dp[i-1]
    if 9<int(S[i-1:i+1])<27 : dp[i] += dp[i-2] if i>1 else 1
    if dp[i]>=MOD : dp[i]%=MOD
print(0 if 0 in dp else dp[-1])