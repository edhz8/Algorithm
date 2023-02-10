G=[[*map(int,input().split())] for _ in '9'*9]
ijs=[(i,j) for i in range(9) for j in range(9) if not G[i][j]]
def rec(n):
    if n==len(ijs):
        for num in range(9):print(*G[num])
        exit(0)
    i,j=ijs[n]
    nums = [0]*10
    for k in range(9): nums[G[i][k]]=nums[G[k][j]]=1
    istep,jstep=(i//3)*3,(j//3)*3
    for k in range(istep,istep+3):
        for l in range(jstep,jstep+3): nums[G[k][l]]=1
    nums = [i for i,num in enumerate(nums) if num==0 and i>0]
    for num in nums:
        G[i][j]=num
        rec(n+1)
        G[i][j]=0
rec(0)
