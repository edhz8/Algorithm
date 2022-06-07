import sys
from collections import deque
input = sys.stdin.readline
N,K=map(int,input().split())
ryans = deque()
ans = float('inf')
for i,v in enumerate(map(int,input().split())):
    if v==2 : continue
    ryans.append(i)
    if len(ryans) == K:
        ans = min(ans,ryans[-1]-ryans[0]+1)
        ryans.popleft()
print(ans if ans != float('inf') else -1)