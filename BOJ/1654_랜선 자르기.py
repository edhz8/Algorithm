K,N = map(int,input().split())
ks,L = [int(input()) for _ in range(K)],0
def SUM(n): return sum([k//n for k in ks])
while 1:
    po = 1
    while 1:
        if  SUM(L+po)>=N: po *=2
        else : 
            po//=2
            if N > SUM(L+po+1): print(L+po);exit(0)
            break
    L += po