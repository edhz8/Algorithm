A,B=map(int,input().split())
a,b=min(A,B),max(A,B)
print(int((a+b)/2*(-a+b+1)))