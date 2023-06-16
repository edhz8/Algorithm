N,B=input().split()
B=int(B)
j=1
answer = 0
for c in reversed(N):
    answer+=(ord(c)-55 if c.isalpha() else int(c))*j
    j*=B
print(answer)