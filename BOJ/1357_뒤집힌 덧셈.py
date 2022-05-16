r=lambda n: int(n[::-1])
a,b=map(r,input().split())
print(r(str(a+b)))