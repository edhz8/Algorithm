n,a,b=int(input()),0,1
if n<2 : print(n)
else :
    for _ in range(n-1) : a,b=b,a+b
    print(b)