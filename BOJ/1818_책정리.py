import bisect
N=int(input())
L=[]
for n in map(int,input().split()):
    if not L or L[-1]<n:L+=[n]
    else:L[bisect.bisect_left(L,n)]=n
print(N-len(L))