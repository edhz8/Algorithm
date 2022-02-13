import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    points = [tuple(map(int,input().split())) for _ in range(N)]
      