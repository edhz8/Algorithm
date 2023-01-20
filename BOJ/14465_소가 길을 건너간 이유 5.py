import sys
input = sys.stdin.readline
N,K,B=map(int,input().split())
bs = set([int(input()) for _ in ' '*B])
s,e=1,K
answer = N
cur = sum([1 for i in range(s,e+1) if i in bs])
while e<N:
    if s in bs : cur-=1
    s+=1
    e+=1
    if e in bs : cur+=1
    answer = min(answer,cur)
print(answer)
