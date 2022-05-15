S = input()
print((sum(+(a!=b) for a,b in zip(S[:-1],S[1:]))+1)//2)