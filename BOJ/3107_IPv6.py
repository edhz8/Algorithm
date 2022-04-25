I = input().replace('::',':!')
L,f,sps=len(I),0,[]
for i in range(L):
    if I[i]==':' and I[f:i] != '':
        sps.append(I[f:i])
        f=i+1
    elif I[i]=='!':
        sps.append(0)
        f=i+1
    elif i==L-1 : sps.append(I[f:])
print(sps)
for i,s in enumerate(sps):
    if i!=0 : print(':',end='')
    if s==0 : print(('0000'+(':0000'*(8-len(sps)) if len(sps)<8 else '') ),end='')
    else : print('0'*(4-len(s))+s,end='')