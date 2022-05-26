from heapq import heappush,heappop
N = int(input())
a,b=map(int,input().split())
num = int(input())
nums = [int(input()) for _ in ' '*num]
q = [(0,0,a,b)]
while q:
    cnt,index,x,y = heappop(q)
    if index == num : print(cnt);break
    t = nums[index]
    heappush(q,(cnt+abs(x-t),index+1,t,y))
    heappush(q,(cnt+abs(y-t),index+1,x,t))