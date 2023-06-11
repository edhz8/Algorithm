a=[s:=input()]
while s:=min(s[:i]+s[i+1:]for i in range(len(s))):a=[s]+a
print(*a)