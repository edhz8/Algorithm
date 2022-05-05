from abc import ABC


def rec(s):
    if s == S : print(1);exit(0)
    if len(s) == len(S) : return
    if s[-1]=='A' : rec(s[:-1])
    if s[0]=='B' : rec(s[1:][::-1])
S,T=input(),input()
rec(T)
print(0)