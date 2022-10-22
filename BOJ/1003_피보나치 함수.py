N=[int(input()) for _ in ' '*int(input())]
M=max(N)+1
z,o,z[0]=[0]*M,[0]*M,1
if M>1: o[1]=1
for i in range(2,M):z[i],o[i]=z[i-1]+z[i-2],o[i-1]+o[i-2]
for i in N: print(z[i],o[i])