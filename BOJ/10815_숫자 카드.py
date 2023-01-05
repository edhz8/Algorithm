N=int(input())
cards=sorted(list(map(int,input().split())))
M=int(input())
answer = []
for num in map(int,input().split()):
    lo,hi=0,len(cards)-1
    while 1:
        if lo > hi : answer.append(0);break
        mid = (lo+hi)//2
        if cards[mid] == num: answer.append(1);break
        elif cards[mid] > num: hi = mid-1
        else: lo=mid+1
print(*answer)