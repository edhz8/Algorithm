N,M,*a=map(int,open(0).read().split())
S,s=0,[0]*M
for d in [0,*a]:S+=d;s[S%M]+=1
print(sum(n*(n-1)//2 for n in s))