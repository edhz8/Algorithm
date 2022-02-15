m,n=-1,int(input())
for i in range(n//5,-1,-1):
    if (n-5*i)%3==0 : 
        m=i+(n-5*i)//3
        break
print(m)