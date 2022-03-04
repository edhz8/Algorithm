N,M=map(int,input().split())
v=[]
def rec(cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(1,N+1):
        v.append(i)
        rec(cnt+1)
        v.pop()
rec(0)