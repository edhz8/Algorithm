def rec(l,cur,N):
    tl = (l-cur)//2
    if N<=tl: return rec(tl,cur-1,N)
    elif N>tl+cur: return rec(tl,cur-1,N-tl-cur)
    else:print("m" if N==tl+1 else "o");exit(0)
N,L,n = int(input()),3,0
while N>L:
    n+=1
    L=2*L+n+3
rec(L,n+3,N)