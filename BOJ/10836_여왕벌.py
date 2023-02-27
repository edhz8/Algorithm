import sys
I,R=sys.stdin.readline,range
M,N=map(int,I().split())
L=[1]*(2*M+1)
for _ in ' '*N:
    z,o,t=map(int,I().split())
    for i in R(o+t):L[i+z]+=(1+(i>=o))
G=[[L[M-1+(j if j else-i)]for j in R(M)]for i in R(M)]
for i in R(M):print(*G[i])