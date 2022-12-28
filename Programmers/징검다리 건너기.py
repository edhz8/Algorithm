from collections import deque
def solution(stones, k):
    q=deque()
    answer = float('inf')
    for i,stone in enumerate(stones):
        while q and q[-1][1]<stone: q.pop()
        q.append([i,stone])
        if q[0][0] <= i-k : q.popleft()
        if k-1<=i : answer = min(answer,q[0][1])
        print(stone,'일때 :',q,answer)
    return answer