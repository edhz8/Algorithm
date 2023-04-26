import sys
input = sys.stdin.readline
N=int(input())
arr=sorted([*map(int,input().split())])
M=int(input())
if sum(arr)<=M : print(max(arr));exit(0)
Min,Max=arr[0],arr[N-1]
bcnt,bsum=[0]*(Max+1),[0]*(Max+1)
for a in arr : bcnt[a]+=1;bsum[a]+=a
for i in range(1,Max+1) : bcnt[i]+=bcnt[i-1];bsum[i]+=bsum[i-1]
start=0
end=Max
k,v=0,0
while start<=end:
    mid = (start+end)//2
    cur=(N-bcnt[mid])*mid + bsum[mid]
    if cur==M : k,v=mid,cur;break
    elif cur < M : 
        start = mid + 1
        if v<cur : k,v=mid,cur
    else : end = mid -1
print(k)