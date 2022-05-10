import sys
from collections import deque
input = sys.stdin.readline
N,M=map(int,input().split())
do,su=deque(),deque()
for _ in range(N):
    d,s=map(int,input().split())
    do.append(d)
    su.append(s)
dg,sg=deque(),deque()
while 1:
    if M==0 : break
    M-=1
    dg.append(do.pop())
    if not do : print('su');exit(0)
    if dg and sg and dg[-1]+ sg[-1] == 5 :
        su.extendleft(dg)
        su.extendleft(sg)
        dg,sg=deque(),deque()
    elif (dg[-1] == 5) or (sg and sg[-1]==5) : 
        do.extendleft(sg)
        do.extendleft(dg)
        dg,sg=deque(),deque()

    if M==0 : break
    M-=1
    sg.append(su.pop())
    if not su : print('do');exit(0)
    if dg and sg and dg[-1]+sg[-1]==5 :
        su.extendleft(dg)
        su.extendleft(sg)
        dg,sg=deque(),deque()
    elif (sg[-1] == 5) or (dg and dg[-1]==5) : 
        do.extendleft(sg)
        do.extendleft(dg)
        dg,sg=deque(),deque()
print('do' if len(do)>len(su) else 'dosu' if len(do)==len(su) else 'su')
