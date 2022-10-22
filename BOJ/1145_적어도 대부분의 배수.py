N,i=input().split(),1
while sum(i%int(n)<1 for n in N)<3:i+=1
print(i)