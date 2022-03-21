from collections import deque
N,K=map(int,input().split())
n=deque(range(1,N+1))
print('<',end='')
while n:
    n.rotate(-(K-1))
    print(n.popleft(),end=', ' if n else '')
print('>')