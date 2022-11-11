N=int(input())
nums=[*map(int,input().split())]
if N==1:print('A');exit(0)
if N==2:
    if nums[0]==nums[1] : print(nums[0])
    else : print('A')
    exit(0)
if N>=3:
    if nums[0]==nums[1] :
        if all(nums[0]==i for i in nums) : print(nums[0])
        else : print('B')
        exit(0)
    a=(nums[2]-nums[1])/(nums[1]-nums[0])
    if int(a)!=a : print('B');exit(0)
    a=int(a)
    b=nums[1]-nums[0]*a
    for i in range(3,len(nums)):
        if nums[i]!=a*nums[i-1]+b : print('B');exit(0)
    print(a*nums[-1]+b)