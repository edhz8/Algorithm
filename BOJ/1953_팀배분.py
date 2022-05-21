import sys
input = sys.stdin.readline
def dfs(index,t):
    ans[index] = t
    v[index] = 1
    for i in range(n):
        if s[index][i] == 1 and v[i] == 0: dfs(i, -t)
n = int(input())
s,v,ans = [[0]*n for _ in ' '*n],[0 for _ in ' '*n],[0 for _ in ' '*n]
for i in range(n):
    for j in list(map(int, input().split()))[1:]:
        s[i][j - 1] = s[j - 1][i] = 1
for i in range(n):
    if v[i] == 0: dfs(i, 1)
print(ans.count(1))
print(*[i+1 for i in range(n) if ans[i]==1])
print(ans.count(-1))
print(*[i+1 for i in range(n) if ans[i] == -1])