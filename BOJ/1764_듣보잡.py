import sys
input = sys.stdin.readline
N,M=map(int,input().split())
ns = set([input() for _ in ' '*N])
ms = []
for _ in ' '*M :
    i=input()
    if i in ns: ms.append(i.strip())
print(len(ms))
print(*sorted(ms),sep='\n')
# 10:37