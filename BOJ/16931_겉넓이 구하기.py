import sys
input = sys.stdin.readline
N,M = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(N)]
ans = N*M
for i in range(N):
    for j in range(M):
        for k in range(1,g[i][j]+1):
            cur = 5
            if k != g[i][j] : cur -=1
            if i>0 and g[i-1][j] >= k : cur -=1 
            if j>0 and g[i][j-1] >= k : cur -=1 
            if i<N-1 and g[i+1][j] >= k : cur -=1 
            if j<M-1 and g[i][j+1] >= k : cur -=1
            ans += cur
print(ans)