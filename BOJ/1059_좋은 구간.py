import bisect
_,*N,n=map(int,open(0).read().split())
N=[0]+sorted(N)
i=bisect.bisect_left(N,n)
print(max(0,(N[i]-n)*(n-N[i-1])-1))