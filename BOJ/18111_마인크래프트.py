import sys
input = sys.stdin.readline
N,M,B=map(int,input().split())
LIMIT = 257
dp = [0 for _ in range(LIMIT)]
for i in range(N):
    for j in map(int,input().split()) : dp[j] += 1
SUM = sum(i*v for i,v in enumerate(dp))
time,height = float('inf'),0
for i in range(LIMIT):
    if i*N*M > SUM+B : break
    plus,minus = 0,0
    for j in range(LIMIT) :
        if i>j : minus += (i-j)*dp[j]
        else : plus += (j-i)*dp[j]
    if plus+B<minus : break
    if time >= plus*2+minus : time,height = plus*2+minus,i
print(time,height)