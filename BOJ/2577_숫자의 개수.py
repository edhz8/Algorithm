n=str(int(input())*int(input())*int(input()))
for i in range(10):
    c=0
    for N in n:
        if N==str(i): c+=1
    print(c)