I=lambda:map(int,input().split())
N,M=I()
A=sorted(I())
B=sorted(I())
i,j=0,0
answer = []
while i<N or j<M:
    if i==N : answer.append(B[j]);j+=1;continue
    if j==M : answer.append(A[i]);i+=1;continue
    if B[j]>=A[i] : answer.append(A[i]);i+=1;continue
    if B[j]<A[i] : answer.append(B[j]);j+=1;continue
print(*answer)