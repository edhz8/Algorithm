A,B,C=map(int,input().split())
def rec(a,b):
    return a%C if b==1 else rec(a,b//2)**2*a%C if b%2 else rec(a,b//2)**2%C
print(rec(A,B))