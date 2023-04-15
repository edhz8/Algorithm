import sys
input = sys.stdin.readline
n = int(input())
C = [[*map(int,input().split())] for _ in ' '*n]
def distance(x1,y1,x2,y2): return(x2-x1)**2+(y2-y1)**2
Min,index = float('inf'),-1
for i in range(n):
    Max = -1
    MaxIndex = -1
    for j in range(n):
        d = distance(C[i][0],C[i][1],C[j][0],C[j][1])
        if Max < d:
            Max = d
            MaxIndex = i
    if Max < Min:
        Min = Max
        index = MaxIndex
print(*C[index])