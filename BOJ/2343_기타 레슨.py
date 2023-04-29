N,M=map(int,input().split())
nums=[*map(int,input().split())]
lo,hi=max(nums),sum(nums)
while lo<hi:
    mid=(lo+hi)//2
    cur,cnt=0,1
    for num in nums:
        cur+=num
        if cur>mid :cur=num;cnt+=1
    if cnt<=M : hi=mid
    else : lo=mid+1
print(lo)