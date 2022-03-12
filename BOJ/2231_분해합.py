n,a=int(input()),0
for i in range(n):
    if i+sum([int(s) for s in str(i)]) == n: a=i;break
print(a)