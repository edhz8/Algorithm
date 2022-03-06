N,v=int(input()),[]
def r():
    if len(v)==N:
        print(*v)
        return
    for i in range(1,N+1):
        if i in v: continue
        v.append(i)
        r()
        v.pop()
r()