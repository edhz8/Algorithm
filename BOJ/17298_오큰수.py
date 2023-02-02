import sys
input = sys.stdin.readline
N=int(input())
A=[-1]*N
nums = [*map(int,input().split())]
for i in range(N-1,-1,-1):
    for j in range(i,-1,-1):
        if i==j:
            if A[i]==-1 : continue
        elif nums[i]>nums[j]: A[j] = nums[i]
print(A)
