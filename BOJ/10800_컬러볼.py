import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
answer = [0]*N
COLORS,SIZES,TOTAL=defaultdict(int),defaultdict(list),0
for size,color,index in sorted([[*map(int,input().split()[::-1]),i] for i in range(N)]):
    current = TOTAL-COLORS[color]-len(SIZES[size])*size+SIZES[size].count(color)*size
    answer[index]=current
    COLORS[color]+=size
    SIZES[size].append(color)
    TOTAL+=size
print(*answer,sep='\n')