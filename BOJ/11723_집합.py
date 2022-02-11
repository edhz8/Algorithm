import sys
input = sys.stdin.readline
l=set()
for _ in range(int(input())):
    i=input().strip()
    if i=='all' : l=set(range(1,21))
    elif i=='empty' : l=set()
    else :
        c,n=i.split()
        n=int(n)
        if c=='add' : l.add(n)
        elif c=='remove' and n in l: l.remove(n)
        elif c=='check' : print(int(n in l))
        elif c=='toggle' :
            if n in l : l.remove(n)
            else : l.add(n)