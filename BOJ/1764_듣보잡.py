import sys
input = sys.stdin.readline
N,M=map(int,input().split())
p,d=[],{}
for _ in range(N): d[input().strip()] = 0
for _ in range(M):
    i=input().strip()
    if i in d : p.append(i)
print(len(p),*sorted(p),sep='\n')