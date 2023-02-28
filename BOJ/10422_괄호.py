N=[int(input()) for _ in ' '*int(input())]
L=max(N)+1
D,D[0]=[0]*L,1
for i in range(2,L+1,2):
    for j in range(2,i+1,2):D[i]+=D[j-2]*D[i-j]
    D[i]%=1000000007
print(*[D[n] for n in N])