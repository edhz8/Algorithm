for _ in ' '*int(input()): print(sum(abs(a-b) for a,b in zip(*[[i for i in range(len(S)) if S[i]=='b']for S in input().split()])))