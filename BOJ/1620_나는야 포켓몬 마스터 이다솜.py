import sys
input = sys.stdin.readline
N,M=map(int,input().split())
d={}
for i in range(1,N+1): 
    s = input().strip()
    d[str(i)],d[s.lower()] = s,i
for i in range(M): print(d.get(input().strip().lower()))