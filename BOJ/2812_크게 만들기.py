N,K = map(int,input().split())
c,A = K,[]
for n in input():
    while c and A and A[-1] < n:
        A.pop()
        c-=1
    A.append(n)
print(*A[:N-K],sep='')