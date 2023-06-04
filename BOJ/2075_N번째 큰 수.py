from heapq import*
q=[]
input=open(0).readline
N=int(input())
for _ in' '*N:
    for n in map(int,input().split()):
        if len(q)<N:heappush(q,n)
        elif q[0]<n:heappop(q);heappush(q,n)
print(q[0]) 