N,nums,ans=int(input()),[1,5,10,50],set()
def rec(c,s,start):
    if c==N: 
        ans.add(s)
        return
    for i in range(start,4):
        rec(c+1,s+nums[i],i) 
rec(0,0,0)
print(len(ans))