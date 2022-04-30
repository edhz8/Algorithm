i  = int(input())
I,c = i,0
while I!=i or c==0: 
    I=I%10*10+((I//10+I%10)%10)
    c+=1
print(c)