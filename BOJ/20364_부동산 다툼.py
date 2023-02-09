import sys
input = sys.stdin.readline
N,Q=map(int,input().split())
v=[0]*(N+1)
for _ in 'Q'*Q:
    num=int(input())
    cur=num
    answer = 0
    while num>0:
        if v[num]: answer=num
        num//=2
    v[cur]=1
    print(answer) 