from bisect import bisect_left
L=[]
for n in map(int,[*open(0)][1].split()):
    if not L or L[-1]<n: L.append(n)
    else: L[bisect_left(L,n)]=n
print(len(L))