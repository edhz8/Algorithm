import sys
input = sys.stdin.readline
N=int(input())
nums,snums=[],set()
for i in input().split():
    i=int(i)
    nums.append(i)
    snums.add(i)
s=sorted(snums)
print(*[s.index(n) for n in nums])