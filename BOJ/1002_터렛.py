for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d,p,m=((x1-x2)**2+(y1-y2)**2)**0.5,r1+r2,abs(r1-r2)
    if d:
        print(1 if d==p or d==m else 2 if d<p and d>m else 0)
    else:
        print(0 if m else -1)