m=lambda:map(int,input().split())
N,M,R=m()
v=[0]*-~N
G=[[]for _ in v]
C=0
q=[0]
for _ in' '*M:a,b=m();G[a]+=[b];G[b]+=[a]
G=[*map(sorted,G)]
G[0]+=[R]
while q:
    for c in G[q.pop(0)]:
        if v[c]==0:C+=1;v[c]=C;q+=[c]
print(*v[1:])