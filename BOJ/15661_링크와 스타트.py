import sys
input = sys.stdin.readline
N = int(input())
g,MIN = [list(map(int,input().split())) for _ in range(N)],float('inf')
dp = [sum([g[j][i]+g[i][j] for j in range(N)]) for i in range(N)]
def rec(start,cnt,cur):
    #global MIN
    MIN = min(MIN,abs(cur))
    if cnt == N//2 : return
    for i in range(start,N+1): rec(i+1,cnt+1,cur-dp[i-1])
rec(1,0,sum([sum(g[i]) for i in range(N)]))
print(MIN)