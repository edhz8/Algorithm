N,M=map(int,input().split())
v,nums = [],sorted(list(map(int,input().split())))
def rec(s,c):
    if c==M :
        print(*v)
        return
    for i in range(s,N):
        v.append(nums[i])
        rec(i+1,c+1)
        v.pop()
rec(0,0)