N,nums,ops,MAX,MIN,giho = int(input()),list(map(int,input().split())),list(map(int,input().split())),-float('inf'),float('inf'),['+','-','*','//']
def rec(cur,cnt):
    global MAX,MIN
    if cnt==N:
        MAX,MIN = max(MAX,cur),min(MIN,cur)
        return
    for i in range(4):
        if ops[i]:
            ops[i]-=1
            rec(eval(str(cur)+giho[i]+str(nums[cnt])) if i<3 else eval(str(abs(cur))+giho[i]+str(nums[cnt]))*(1 if cur>0 else -1),cnt+1)
            ops[i]+=1
rec(nums[0],1)
print(MAX,MIN,sep='\n')