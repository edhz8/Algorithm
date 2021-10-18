from collections import defaultdict
d,N=defaultdict(int),1
for _ in range(int(input())): d[input()[0]]+=1
for k,v in sorted(d.items()):
    if v>4 : N=0;print(k,end='')
if N : print('PREDAJA')