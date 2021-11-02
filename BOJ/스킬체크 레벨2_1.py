from collections import deque
def solution(priorities, location):
    que = deque([(index,priority) for index,priority in enumerate(priorities)])
    cnt = 0
    while que:
        POP=True
        [I,P] = que[0]
        for i in range(1,len(que)):
            [i,p] = que[i]
            if p>P : POP = False;break
        if POP :
            [I,P] = que.popleft()
            cnt+=1
            if I == location : return cnt
        else : que.rotate(-1)