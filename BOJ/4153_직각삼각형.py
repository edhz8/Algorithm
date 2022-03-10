while (I:=input())!='0 0 0':
    a,b,c=sorted(map(int,I.split()))
    print(['wrong','right'][a**2+b**2==c**2])