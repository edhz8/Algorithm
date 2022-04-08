import sys
input = sys.stdin.readline
N,L = map(int,input().split())
trees = list(map(int, input().split()))
S,E = 0,max(trees)
while S <= E:
    M = (S+E)//2
    tree = sum(i-M for i in trees if i > M)
    if tree >= L: S = M + 1
    else: E = M - 1
print(E)