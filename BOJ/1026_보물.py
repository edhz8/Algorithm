import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int,input().split()),reverse=True)
B = sorted(map(int,input().split()))
print(sum([A[i]*B[i] for i in range(N)]))