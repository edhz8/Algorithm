from heapq import heappop,heappush
from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    maxq,minq,v=[],[],defaultdict(bool)
    for i in range(int(input())):
        cmd, num = input().strip().split()
        num = int(num)
        if cmd == 'I':
            heappush(minq,(num,i))
            heappush(maxq,(-num,i))
            v[i] = True
        else :
            while maxq and minq:
                n,k=heappop(maxq if num == 1 else minq)
                if v[k] :
                    v[k] = False
                    break

    for q in [maxq,minq]: 
        while q and not v[q[0][1]]:heappop(q)
    print(*[heappop(maxq)[0]*-1,' ',heappop(minq)[0]] if maxq and minq else 'EMPTY',sep='')
