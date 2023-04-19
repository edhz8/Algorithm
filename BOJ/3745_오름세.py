from bisect import bisect_left
while 1:
    try :
        N,L=int(input()),[]
        for n in map(int,input().split()) :
            if not L or L[-1]<n : L.append(n)
            else : L[bisect_left(L,n)]=n
        print(len(L))
    except : break