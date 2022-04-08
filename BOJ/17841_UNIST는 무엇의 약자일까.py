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
    for j in range(s,e): dp[j] += dp[s-1] if s>1 else 1
    for i in range(5): dp[i]%=(10**9+7)
print(dp[4])
print(dp)