N,L=map(int,input().split())
def S(L): return L*(L-1)//2
while L<101 and (N-S(L))%L!=0: L+=1
if L>100: print(-1);exit(0)
if L>100 or N<S(L): print(-1);exit(0)
add=(N-S(L))//L
print(*[i+add for i in range(L)])