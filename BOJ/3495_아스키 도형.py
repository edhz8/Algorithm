h,w=map(int,input().split())
ans=0
for _ in range(h):
    cur=0
    for c in input():
        if c in ['/','\\'] : cur+=1
        elif cur&1 : ans +=1
    ans+=cur//2
print(ans)