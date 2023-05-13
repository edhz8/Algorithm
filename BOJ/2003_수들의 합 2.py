N,M=map(int,input().split())
nums=[0]+[*map(int,input().split())]
for i in range(1,N+1): nums[i] += nums[i-1]
answer=0
lo,hi=0,1
while lo<=hi and hi<=N:
    cur = nums[hi] - nums[lo]
    if cur >= M : lo += 1
    else : hi += 1
    answer += (cur==M)
print(answer)