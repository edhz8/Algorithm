import sys
input = sys.stdin.readline
N,M=map(int,input().split())
arr,v = [[] for _ in ' '*N],[]
for _ in ' '*M:
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
def dfs(i,depth):
    if depth == 4 : print(1);exit(0)
    for j in arr[i]:
        if j in v: continue
        v.append(j)
        dfs(j,depth+1)
        v.remove(j)
for i in range(N):
    v=[i]
    dfs(i,0)
print(0)