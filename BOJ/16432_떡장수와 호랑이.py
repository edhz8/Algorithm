import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
duks = [list(map(int,input().split()))[1:] for _ in ' '*N]
ans,dp = [0]*N,[[0]*10 for _ in ' '*N]
def rec(i,p) :
    if i == N : 
        print(*ans)
        exit(0)
    for duk in duks[i]:
        if duk!=p and dp[i][duk]^1 :
            dp[i][duk] = 1
            ans[i] = duk
            rec(i+1,duk)
rec(0,0)
print(-1)