for _ in range(int(input())):
    s={}
    for _ in range(int(input())):
        k,v=input().split()
        s[int(k)]=v
    print(sorted(s.items())[-1][1])