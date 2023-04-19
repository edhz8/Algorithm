from bisect import bisect_left
N,L=int(input()),[]
for n in map(int,input().split()):
    if not L or L[-1]<n: L.append(n)
    else: L[bisect_left(L,n)]=n
print(N-len(L))