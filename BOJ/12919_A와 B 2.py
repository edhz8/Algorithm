S=input()
def R(t):
    if t==S:print(1);exit(0)
    if len(t)==len(S):return
    if t[0]=='B':R(t[:0:-1])
    if t[-1]=='A':R(t[:-1])
R(input())
print(0)