I,M=-1,-1
for i in range(9):
    t=int(input())
    if t > M : I,M=i,t
print(M,I+1,sep='\n') 