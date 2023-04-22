N=int(input())
arr=sorted(map(int,input().split()))
L,R=0,len(arr)-1
answer=[float('inf'),float('inf')]
while L<R and sum(answer)!=0:
    if abs(sum(answer))>abs(arr[L]+arr[R]): answer=[arr[L],arr[R]]
    if arr[L]+arr[R]>0 : R-=1
    elif arr[L]+arr[R]<0 : L+=1
print(*answer)