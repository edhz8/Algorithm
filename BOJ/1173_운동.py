N,m,M,T,R=map(int,input().split())
cur=m
time = 0
while N:
    if cur+T<=M : cur += T ; N -= 1
    elif cur==m : print(-1);exit()
    else : cur=max(m,cur-R)
    time += 1
print(time)