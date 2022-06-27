import sys
from collections import Counter
input = sys.stdin.readline
n,nums,ans=int(input()),sorted(list(map(int,input().split()))),0
c=Counter(nums)
for i in range(len(nums)):
    l,r=i+1,n-1
    while l<r:
        S=nums[i]+nums[l]+nums[r]
        if S>0 : r-=1
        elif S<0 : l+=1
        else : 
            ans += (r-l) if nums[l]==nums[r] else c[nums[r]]
            l+=1
print(ans)