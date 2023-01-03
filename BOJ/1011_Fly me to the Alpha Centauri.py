for _ in range(int(input())):
    x,y=map(int,input().split())
    y-=x
    i=1
    while i*i<y: i+=1
    i-=1
    if y<=i*(i+1):print(i*2)
    else:print(i*2+1)