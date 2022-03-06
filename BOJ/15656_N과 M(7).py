N,M=map(int,input().split())
nums = sorted(list(map(int,input().split())))
v = []
def rec(c):
    if c==M:
        print(*v)
        return
    for i in range(N):
        v.append(nums[i])
        rec(c+1)
        v.pop()
rec(0)