N,S=map(int,input().split())
nums = [*map(int,input().split())]
l,r,s,a=0,0,0,float('inf')
while 1:
    if s>=S:a=min(a,r-l);s-=nums[l];l+=1
    elif r==N: break
    else:s+=nums[r];r+=1
print(a if a!=float('inf') else 0)