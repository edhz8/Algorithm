from collections import deque
def solution(n, computers):
    visited = [False]*n
    cnt = 0
    for i in range(n):
        if visited[i] : continue
        cnt+=1
        que = deque([i])
        while que:
            poped = que.popleft()
            visited[poped] = True
            computer = computers[poped]
            for j in range(i+1,n):
                if computer[j] and (not visited[j]): que.append(j)
    return cnt