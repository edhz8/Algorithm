N=int(input())
if N==1 : print(0);exit(0)
nums=[1 for i in range(N+1)]
for i in range(2,int(N**0.5)+1):
    if nums[i]:
        j=2
        while i*j<=N:
            nums[i*j]=0
            j+=1
nums=[i for i in range(2,N+1) if nums[i]]
L=len(nums)
l,r,s,a=0,0,nums[0],0
while 1:
    if s==N: a+=1
    if s>N:
        s-=nums[l]
        l+=1
    else:
        r+=1
        if r==L: break
        s+=nums[r]
print(a)