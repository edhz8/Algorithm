N,M,S,n,answer,i=int(input()),int(input()),input(),0,0,0
while i<=M-3:
    if S[i:i+3]=='IOI':
        n+=1
        i+=1
        if n==N:answer+=1;n-=1
    else:n=0
    i+=1
print(answer)