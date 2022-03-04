N,M=map(int,input().split())
v=[]
def rec(s,c):
    if c==M:
        print(*v)
        return
    for i in range(s,N+1):
        v.append(i)
        rec(i,c+1)
        v.pop()
rec(1,0)