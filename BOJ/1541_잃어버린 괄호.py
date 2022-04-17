num = []
for i in input().split('-'):
    cnt = 0
    for j in i.split('+'): cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):n -= num[i]
print(n)