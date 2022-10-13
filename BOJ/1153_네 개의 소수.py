N=int(input())
prime=[1]*N
for i in range(2,int(N**0.5)+1):
    if prime[i]:
        for j in range(i+i,N,i): prime[j]=0
prime=[i for i in range(2,len(prime)) if prime[i]]
cur=[]
def rec(index):
    if len(cur)>4:return
    if sum(cur)==N and len(cur)==4: print(*cur);exit(0)
    for i in range(index,len(prime)):
        if sum(cur)+prime[i]<=N: 
            cur.append(prime[i])
            rec(i)
            cur.pop(-1)
for i in range(len(prime)):
    cur.append(prime[i])
    rec(i)
    cur.pop()
print(-1)