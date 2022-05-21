N,K=map(int,input().split())
ans=0
while bin(N).count('1')>K:
    p=2**bin(N)[::-1].find('1')
    ans+=p
    N+=p
print(ans)