N,M=map(int,input().split())
nums=[*map(int,input().split())]
LEFT,RIGHT=0,60000000000
while LEFT<RIGHT:
    MIDDLE=(LEFT+RIGHT)//2
    if sum(MIDDLE//n for n in nums)+M>=N : RIGHT=MIDDLE
    else : LEFT=MIDDLE+1
cnt=M+sum((LEFT-1)//n for n in nums)
for i,n in enumerate(nums,1):
    if LEFT%n==0:cnt+=1
    if cnt==N:print(i);break