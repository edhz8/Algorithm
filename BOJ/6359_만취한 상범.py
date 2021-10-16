for _ in range(int(input())):
    n=int(input())
    r=[False]*(n+1)
    for j in range(1,n+1):
        for i in range(j,n+1): 
            if i%j==0 : r[i] = not r[i] 
    print(r[1:].count(True))