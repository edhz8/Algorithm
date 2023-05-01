from itertools import combinations
N,K=map(int,input().split())
K-=5
if K<0 : print(0);exit(0)
antic=set(['a','n','t','i','c'])
words=[]
alpha=set()
answer=0
t=0
for _ in ' '*N:
    cur=set(input())-antic
    if not cur : t+=1 
    elif len(cur)<=K : words.append(cur)
    alpha.update(cur)
if len(alpha)<=K : print(N);exit(0)
for als in combinations(alpha,K):
    als=set(als)
    answer = max(answer,sum(1 for word in words if als>=word))
print(t+answer)