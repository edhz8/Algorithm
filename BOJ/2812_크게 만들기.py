N,K=map(int,input().split())
k,A=K,[]
for n in input():
    while K and A and A[-1]<n:A.pop();K-=1
    A+=n
print(''.join(A[:N-k]))