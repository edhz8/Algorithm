m=lambda:[*map(int,input().split())]
m()
n=0
A=[n:=n+i for i in[0]+m()]
for _ in' '*m()[0]:i,j=m();print(A[j]-A[i-1])