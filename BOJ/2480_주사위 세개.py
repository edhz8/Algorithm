a,b,c=map(int,input().split())
if a==b and b==c : print(10000+a*1000)
elif a!=b and b!=c and a!=c: print(100*max(a,b,c))
else:print(1000+(b if b==c or a==b else a)*100)