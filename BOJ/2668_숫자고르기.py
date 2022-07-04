N=int(input())
l,p=[0]+[int(input()) for _ in ' '*N],[]
def dfs(c,s):
    v[c]=1
    if v[l[c]]^1: dfs(l[c],s)
    elif l[c]==s: p.append(s)
for i in range(1,N+1): 
    v=[0]*(N+1)
    dfs(i,i)
print(len(p),*p)