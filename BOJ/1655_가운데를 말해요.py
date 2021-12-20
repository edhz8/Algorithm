import heapq
import sys
I,L,R = sys.stdin.readline,[],[]
for _ in range(int(I())):    
    if len(L) == len(R) : heapq.heappush(L,-int(I()))
    else : heapq.heappush(R,int(I()))
    if R and -L[0] > R[0] :
        toL,toR=heapq.heappop(R),-heapq.heappop(L)
        heapq.heappush(L,-toL)
        heapq.heappush(R,toR)
    print(-L[0])