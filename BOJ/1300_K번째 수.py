N,k=eval('int(input()),'*2)
L,R=1,k
while L<R:M=(L+R)//2;L,R=[L,M+1,M,R][sum(min(M//i,N)for i in range(1,N+1))<k::2]
print(L)