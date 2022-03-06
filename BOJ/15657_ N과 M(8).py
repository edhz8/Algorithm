N,M=map(int,input().split())
nums = sorted(list(map(int,input().split())))
v = []
def rec(s,c):
    if c==M:
        print(*v)
        return
    for i in range(s,N):
        v.append(nums[i])
        rec(i,c+1)
        v.pop()
rec(0,0)