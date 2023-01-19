X,Y=map(int,input().split())
Z = int(Y*100/X)
t=0
exp=0
def per(t): return int((Y+t)*100/(X+t))
if Z>=99: print(-1);exit(0)
while per(t) == per(t+1):
    while Z == per(t+2**exp):
        t+=pow(2,exp)
        exp+=1
    exp=0
print(t+1)