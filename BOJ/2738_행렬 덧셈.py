N,M=map(int,input().split())
g=[list(map(int,input().split())) for _ in '  '*N]
print(*[g[i][j]+g[i+N][j] for i in range(N) for j in range(M)])