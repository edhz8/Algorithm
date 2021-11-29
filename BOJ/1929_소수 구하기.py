import math
m,n=map(int,input().split())
for i in range(m,n+1):
    P=i>1
    for j in range(2,int(math.sqrt(i))+1) :
        if i%j == 0 : P=0;break
    if P : print(i)