from math import factorial as f
def com(n,r) : return f(n)//(f(n-r)*f(r))
N,M,K=map(int,input().split())
if K==0 : print(com(N+M-2,min(N,M)-1))
else :
    r,c=divmod(K-1,M)
    before = com(r+c,min(r,c)) if min(r,c)>0 else 1
    after = com(N-r-1+M-c-1,min(N-r-1,M-c-1)) if N-r>1 and M-c>1  else 1
    print(before * after)