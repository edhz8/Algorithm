from collections import deque
A,B = map(int,input().split())
que = deque([(A,1)])
while que:
    [Num,Try] = que.popleft()
    if B in [Num*2,Num*10+1] : print(Try+1);exit()
    
    if Num*2 < B : que.append((Num*2,Try+1))
    if Num*10+1 < B : que.append((Num*10+1,Try+1))
print(-1)