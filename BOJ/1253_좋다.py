n = int(input())
L = list(map(int,input().split()))
dic = {}
for i in range(n): dic.setdefault(L[i], set()).add(i)
# print(dic)
for i in range(n):
    for j in range(i+1, n):
        v = L[i] + L[j]
        if v in dic: dic[v]&= {i, j}
# print(dic)
print(n - sum(map(len, dic.values())))