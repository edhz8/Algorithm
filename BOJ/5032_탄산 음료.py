e,f,c=map(int,input().split())
ans,bottle=0,e+f
while True:
    t = (bottle//c)
    bottle = t + (bottle%c)
    ans+=t
    if bottle<c : break
print(ans)