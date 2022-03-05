N,M=map(int,input().split())
v,nums = [],sorted(list(map(int,input().split())))
def rec(c):
    if c==M :
        print(*v)
        return
    for i in range(N):
        if nums[i] in v: continue
        v.append(nums[i])
        rec(c+1)
        v.pop()
rec(0)