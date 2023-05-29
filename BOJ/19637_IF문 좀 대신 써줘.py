from bisect import*
i=open(0).readline
N,M=map(int,i().split())
K,V=zip(*[i().split()for _ in' '*N])
V=[*map(int,V)]
for _ in' '*M:print(K[bisect_left(V,int(i()))])