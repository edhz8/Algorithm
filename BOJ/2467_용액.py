N=int(input())
nums = [*map(int,input().split())]
i,j=0,len(nums)-1
answer=[nums[i],nums[j]]
while i<j:
    cur = nums[i]+nums[j]
    if abs(cur)<abs(sum(answer)): answer=[nums[i],nums[j]]
    if cur<0 : i+=1
    elif cur>0 : j-=1
    else : break
print(*answer)