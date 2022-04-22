N = int(input())
g = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    v,q = [0 for _ in range(N)],[]
    for j in range(N) :
        if g[i][j] : q.append(j)
    while q:
        num = q.pop(0)
        v[num] = 1
        for j in range(N):
            if g[num][j] and not v[j]:
                q.append(j)
                g[i][j] = 1
for i in range(N) : print(*g[i])