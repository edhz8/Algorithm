import sys
input = sys.stdin.readline
N,M = map(int,input().split())
n=list(map(int,input().split()))+[0]
for i in range(1,N): n[i] += n[i-1]
for _ in range(M):
    x,y=map(int,input().split())
    print(n[y-1]-n[x-2])