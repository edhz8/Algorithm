G=int(input())
a=L=1
while a*a<G:a+=1
while 2*a-1<=G:
    b=a
    while((T:=a*a-b*b)<=G)*b:
        if T==G:print(a);L=0
        b-=1
    a+=1
if L:print(-1)