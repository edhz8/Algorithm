from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pops=list(map(int,input().split()))
nums,cnt = deque([n+1 for n in range(N)]),0
for p in pops:
    while True:
        if nums[0] == p :
            nums.popleft()
            break
        nums.rotate(-1 if nums.index(p)<=len(nums)//2 else 1)
        cnt +=1
print(cnt)