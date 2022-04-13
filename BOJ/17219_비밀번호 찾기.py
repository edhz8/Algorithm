import sys
input = sys.stdin.readline
N,M = map(int,input().split())
p=dict()
for _ in range(N):
    l = input().strip().split()
    p[l[0]] = l[1]
print(*[p[input().strip()] for _ in range(M)],sep='\n')