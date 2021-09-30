a,b,c=int(input()),[*map(int,list(input()))],0;b.reverse()
for i in range(3):b[i]*=a;c+=b[i]*10**i
print(*b,c,sep='\n')