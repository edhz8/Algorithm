import sys
input = sys.stdin.readline
N, M = map(int, input().split())
master = list(map(int, input().split()))
total = [0] * N
for m in range(M):
    i, w = map(int, input().split())
    total[i - 1] += w
for n in range(1, N):
    slave = master[n] - 1
    total[n] += total[slave]
print(*total)