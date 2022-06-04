import sys
from math import ceil
input = sys.stdin.readline
MIN,MAX = map(int,input().split())
ans = MAX-MIN+1
v = [0]*(MAX-MIN+1)
i=2
while i*i <= MAX:
    ii = i*i
    j = ceil(MIN/ii)
    while ii*j <= MAX:
        if v[ii*j-MIN]^1:
            v[ii*j-MIN]=1
            ans-=1
        j+=1
    i+=1        
print(ans)