def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
def solution(nums):
    ans=0
    for a in range(len(nums)-2):
        for b in range(a+1,len(nums)-1):
            for c in range(b+1,len(nums)): ans+=isPrime(nums[a]+nums[b]+nums[c])
    return ans