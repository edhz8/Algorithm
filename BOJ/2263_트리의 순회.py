import sys
I = sys.stdin.readline
n=int(I())
graph,graph[1] =[0 for _ in range(n+1)],-1
for _ in range(n-1):
    a,b = map(int,I().split())
    if a>b: a,b=b,a
    if graph[a]: graph[b]=a
    else : graph[a]=b
for _ in range(int(I())):
    a,b = map(int,I().split())
    a_ans=[a]
    while a != 1:
        a=graph[a] 
        a_ans.append(a)
    while True:
        if b in a_ans : print(b);break
        else : b=graph[b]