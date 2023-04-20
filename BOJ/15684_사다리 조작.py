import sys
input = sys.stdin.readline
def check():
    for i in range(n):
        I = i 
        for j in range(h):
            if G[j][I]: I += 1
            elif I > 0 and G[j][I - 1]: I -= 1
        if I != i: return False
    return True

def dfs(cnt, x, y):
    global ans
    if ans <= cnt: return
    if check(): ans = min(ans, cnt);return
    if cnt==3 : return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n - 1):
            if G[i][j] == 0:
                G[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                G[i][j] = 0


n,m,h=map(int, input().split())
G = [[0]*n for _ in ' '*h]
for _ in ' '*m:
    a,b=map(int, input().split())
    G[a-1][b-1]=1

ans = 4
dfs(0, 0, 0)
print(ans if ans <= 3 else -1)