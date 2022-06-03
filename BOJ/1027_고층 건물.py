N = int(input())
hs = list(map(int,input().split()))
L = len(hs)
ans = 0
for i in range(L):
    l,r=0,0
    gl,gr=-float('inf'),-float('inf')
    for j in range(i-1,-1,-1):
        gc = (hs[j]-hs[i])/(i-j)
        if gl<gc:
            l+=1
            gl = gc
    for j in range(i+1,L):
        gc = (hs[j]-hs[i])/(j-i)
        if gr<gc :
            r+=1
            gr = gc
    ans = max(ans,l+r)
print(ans)