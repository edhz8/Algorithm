Y=M=0
_,b=open(0)
for n in map(int,b.split()):Y+=10*(n//30+1);M+=15*(n//60+1)
print(['YM'[Y>M],'Y M'][Y==M],min(Y,M))