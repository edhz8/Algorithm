I,R=input,range
t,n,N,m,M,P=int(I()),int(I()),[*map(int,I().split())],int(I()),[*map(int,I().split())],{}
for i in R(n):
    s=0
    for j in N[i:]:s+=j;P[s]=P.get(s,0)+1 
print(sum(P.get(t-sum(M[j:i]),0)for i in R(m+1)for j in R(i)))