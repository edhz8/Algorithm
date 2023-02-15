n,w,L=map(int,input().split())
T=[*map(int,input().split())]
B=[0]*w
A=0
while sum(B)!=0 or T:B.pop(0);B.append(T.pop(0) if T and sum(B)+T[0]<=L else 0);A+=1
print(A)
