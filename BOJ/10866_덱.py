import sys
from collections import deque
N = deque()
input = sys.stdin.readline
for _ in range(int(input())):
    l = input().split()
    cmd=l[0]
    if cmd == 'push_front' : N.appendleft(l[1])
    elif cmd == 'push_back' : N.append(l[1])
    elif cmd == 'pop_front' : print(N.popleft() if N else -1)
    elif cmd == 'pop_back' : print(N.pop() if N else -1)
    elif cmd == 'size' : print(len(N))
    elif cmd == 'empty' : print(+(len(N)==0))
    elif cmd == 'front' : print(N[0] if N else -1)
    elif cmd == 'back' : print(N[-1] if N else -1)