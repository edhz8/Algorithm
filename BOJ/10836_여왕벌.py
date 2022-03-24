M,N=map(int,input().split())
ans = [[1 for _ in range(M)] for _ in range(M)]
for _ in range(N):
    line,g = [],[[0 for _ in range(M)] for _ in range(M)]
    for i,v in enumerate(map(int,input().split())): line += [i for _ in range(v)]
    for i in range(2*M-1):
        if i<M : g[M-1-i][0] = line[i]
        else : g[0][i-M+1] = line[i]
    for i in range(M):
        for j in range(M):
            if i and j : g[i][j] = max(g[i-1][j],g[i][j-1],g[i-1][j-1])
            ans[i][j] += g[i][j]
for i in range(M): print(*ans[i])