import collections as c
C = c.deque(range(1,int(input())+1))
while len(C)>1:
    C.popleft()
    C.rotate(-1)
print(*C)