N,K=map(int,input().split())
L=[*map(int,input().split())]
cur = sum(L[:K])
answer = cur
for i in range(N-K):
    cur += (L[i+K] - L[i])
    answer = max(answer,cur)
print(answer)