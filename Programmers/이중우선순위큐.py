from heapq import heappop,heappush
from collections import defaultdict
def solution(operations):
    maxq,minq,v=[],[],defaultdict(bool)
    for i,operation in enumerate(operations):
        cmd,num = operation.split()
        num = int(num)
        if cmd == 'I':
            heappush(minq,(num,i))
            heappush(maxq,(-num,i))
            v[i] = True
        else :
            while maxq and minq:
                n,k=heappop(maxq if num == 1 else minq)
                if v[k] :v[k] = False;break
    for q in [maxq,minq]: 
        while q and not v[q[0][1]]:heappop(q)
    return [heappop(maxq)[0]*-1,heappop(minq)[0]] if maxq and minq else [0,0]