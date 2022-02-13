for _ in range(int(input())):
    a,b=map(int,input().split())
    a%=10
    if a==0 : print(10)
    elif a in [1,5,6] : print(a)
    elif a in [4,9]:
        b%=2
        print(a if b==1 else pow(a,2)%10)
    else:
        b%=4
        print(pow(a,4 if b==0 else b)%10)