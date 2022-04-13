from math import factorial
n,a=str(factorial(int(input())))[::-1],0
for c in n:
    if c!='0' :break
    else : a+=1
print(a)