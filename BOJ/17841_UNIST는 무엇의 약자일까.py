import sys
input = sys.stdin.readline
N,S,ans = int(input()),'UNIST',0
dp = [0 for _ in range(5)]
for n in range(N):
    cur,s,e=input().strip(),0,0
    for i in range(5):
        r = 0
        if S[i] == cur[0] :
            while r<len(cur) and i+r<5 and S[i+r] == cur[r] : r +=1
            s,e=i,i+r
            break
    for i in range(s,e): dp[i] += dp[i-1] if i == s and s>1 and dp[i-1] else 1
print(dp[4]%((10**9)+7))