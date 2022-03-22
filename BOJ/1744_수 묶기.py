N=int(input())
nums,ans,minus,zeros = sorted([int(input()) for _ in range(N)]),0,[],0
while nums:
    c=nums.pop(0)
    if c <0 : minus.append(c)
    elif c == 0 : zeros += 1
    elif c == 1 : ans += c
    else : nums.insert(0,c);break
while len(minus)>1: ans += minus.pop(0) * minus.pop(0)
if len(minus) > zeros : ans += sum(minus[zeros:])  
while len(nums)>1: ans += nums.pop() * nums.pop()
ans += sum(nums)
print(ans)