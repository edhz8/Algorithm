NM,*G=open(0)
N,M=map(int,NM.split())
print(max(sum(all(G[i][j]=='.'for i in range(N))for j in range(M)),sum(all(G[i][j]=='.'for j in range(M))for i in range(N))))