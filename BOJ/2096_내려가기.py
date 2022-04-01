import sys
input = sys.stdin.readline
N,a,b,c,A,B,C = int(input()),0,0,0,0,0,0
for _ in range(N):
    ia,ib,ic = map(int,input().split())
    ma,mb,mc=min(a,b),min(a,b,c),min(b,c)
    Ma,Mb,Mc=max(A,B),max(A,B,C),max(B,C)
    a,b,c = ia+ma,ib+mb,ic+mc
    A,B,C = ia+Ma,ib+Mb,ic+Mc
print(max(A,B,C),min(a,b,c))