import sys
from collections import defaultdict
I = sys.stdin.readline
weights=defaultdict(int)
weights2=defaultdict(int)
n = int(I())
if n==1 : print(0);exit(0)
for line in reversed([I() for _ in range(n-1)]):
    parent,son,weight=map(int,line.split())
    weights2[parent]+=(weight+weights[son])
    weights[parent] = max(weights[parent],weight+weights[son])
print(max(weights2.items(),key= lambda x : x[1])[1])