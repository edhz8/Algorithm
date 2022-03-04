N,M=map(int,input().split())
v=[]
def rec(start,cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(start,N+1):
        v.append(i)
        rec(i+1,cnt+1)
        v.pop()
rec(1,0)