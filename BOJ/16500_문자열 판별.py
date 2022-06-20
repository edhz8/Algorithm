from re import A
from idna import alabel


S=input()
L=len(S)
E=[[] for _ in ' '*L]
v=[0]*L
for _ in ' '*int(input()):
    s = input()
    l = len(s)
    for i in range(L-l+1):
        if s == S[i:i+l] : E[i].append(i+l-1)
def rec(I):
    for e in E[I]: 
        if e == L-1 : print(1);exit(0)
        if v[e+1]^1 : 
            rec(e+1)
            v[e+1] = 1
rec(0)
print(0)