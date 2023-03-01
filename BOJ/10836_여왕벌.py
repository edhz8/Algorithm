import sys
I,R=sys.stdin.readline,range
M,N=map(int,I().split())
L=[1]*(2*M-1)
for _ in ' '*N:
    z,o,t=map(int,I().split())
    for i in R(o+t):L[i+z]+=(1+(i>=o))
for i in R(M):print(L[M-1-i],*L[M:])