import sys
input = sys.stdin.readline
N,M=map(int,input().split())
s=set()
for _ in range(N): s.add(input().rstrip())
for _ in range(M):
    for word in input().split(','):
        word = word.rstrip()
        if word in s: s.remove(word)
    print(len(s))
    print(s)
