N=int(input())
nums=sorted(map(int,input().split()))
ABS=float('inf')
answer = []
for i in range(N):
    j,k=i+1,N-1
    while j<k:
        cur = nums[i]+nums[j]+nums[k]
        if abs(cur)<ABS: ABS,answer = abs(cur),[nums[i],nums[j],nums[k]]
        if cur<0 : j += 1
        else : k -= 1
print(*answer)