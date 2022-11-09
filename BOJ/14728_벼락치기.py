I=lambda:map(int,input().split())
N,T=I()
D=[0]*(T+1)
for _ in ' '*N:
    K,S=I()
    for i in range(T,K-1,-1):D[i]=max(D[i],S+D[i-K])
print(max(D))