import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
B = deque(list(map(int,input().split())))
R = deque([0 for _ in range(N)])
cnt = 0
while B.count(0) < K:
    cnt +=1
    B.rotate(1)
    R.rotate(1)
    R[N-1] = 0
    for i in range(N-2,-1,-1):
        if R[i]==1 and R[i+1]==0 and B[i+1]>0:
            R[i+1] = 1
            R[i] = 0
            B[i+1] -=1
    R[N-1] = 0
    if B[0]>0 and R[0]==0 : 
        R[0] = 1
        B[0] -= 1
print(cnt)