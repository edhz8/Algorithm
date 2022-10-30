N,M=map(int,input().split())
W,D,D[0]=[0]+[*map(int,input().split())],[10001]*(N+1),0
for i in range(N):
    for s in[W[j]+W[k] for j in range(M+1) for k in range(j+1,M+1)]:
        if(I:=i+s)<=N:D[I]=min(D[I],D[i]+1)
print(D[N]if D[N]<10001 else-1)