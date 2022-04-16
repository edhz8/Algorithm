for _ in range(int(input())):
    H,W,N=map(int,input().split())
    d,m=divmod(N,H)
    if N%H==0 : d,m=N//H-1,H
    print('{0}{1:0>2}'.format(m,d+1))