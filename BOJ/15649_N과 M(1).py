N,M = map(int,input().split())
v=[]
def rec(n):
    if n==M : 
        print(*v)
        return
    for i in range(1,N+1):
        if i in v : continue
        v.append(i)
        rec(n+1)
        v.pop()
rec(0)