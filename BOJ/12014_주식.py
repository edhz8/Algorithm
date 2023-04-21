import bisect
for t in range(int(input())):
    L,N,K=[],*map(int,input().split())
    for n in map(int,input().split()):
        if not L or L[-1]<n:L.append(n)
        else:L[bisect.bisect_left(L,n)]=n
    print('Case #%s\n%d'%(t+1,len(L)>=K))