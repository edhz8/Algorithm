I,J=input,int
N=J(I())
A=I().split()
G=[[0]*N for _ in range(N)]
def d(s,e): 
    while 0<=s and e<N and A[s]==A[e]:G[s][e]=1;s-=1;e+=1
for i in range(N):d(i,i);d(i,i+1)
for _ in ' '*J(I()):s,e=map(J,I().split());print(G[s-1][e-1])