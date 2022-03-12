n = int(input())
N,M,i,prt = [int(input()) for _ in range(n)],[],1,''
while i<=n:
    if not M or N[0] != M[-1]:
        M.append(i)
        i+=1
        prt+='+'
    else : 
        M.pop()
        N.pop(0)
        prt+='-'
for x,y in zip(N,M[::-1]):
    if x==y : prt+='-'
    else : prt = 'NO';break
print(*prt,sep='' if prt=='NO' else '\n')