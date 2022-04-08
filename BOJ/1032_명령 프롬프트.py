N,S=int(input()),list(input())
for _ in range(N-1):
    for i,c in enumerate(input()):
        if S[i] != c : S[i] = '?'
print(*S,sep='')