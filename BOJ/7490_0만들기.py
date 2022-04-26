def rec(n,sik):
    global siks,N
    if n==N:
        if eval(sik.replace(' ',''))==0 : siks.append(sik)
        return
    for op in ['+','-',' ']: rec(n+1,sik+op+str(n+1))
for _ in range(int(input())):
    N,siks=int(input()),[]
    rec(1,'1')
    for sik in sorted(siks) : print(sik)
    print()