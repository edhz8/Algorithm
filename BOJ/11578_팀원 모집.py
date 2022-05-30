n,m=map(int,input().split())
t,nums,MIN = sum(1<<i for i in range(n)),[],float('inf')
for i in range(m) :
    t=0
    for j in map(int,input().split()[1:]) : t|= (1<<(j-1))
    nums.append(t)
def rec(num,cnt,depth):
    global MIN
    if depth==m :
        if num==t : MIN = min(MIN,cnt)
        return
    rec(num,cnt,depth+1)
    rec(num|nums[depth],cnt+1,depth+1)
rec(0,0,0)
print(-1 if MIN==float('inf') else MIN)