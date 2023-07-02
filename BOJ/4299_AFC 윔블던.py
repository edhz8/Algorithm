a,b=map(int,input().split())
print(*[d:=(c:=a+b)//2,-1,d-b][c&1or a<b::2])