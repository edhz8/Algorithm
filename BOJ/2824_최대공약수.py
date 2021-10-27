import math
tn,tm=1,1
input()
for n in list(map(int,input().split())) : tn*=n
input()
for m in list(map(int,input().split())) : tm*=m
print(str(math.gcd(tn,tm))[-9:])