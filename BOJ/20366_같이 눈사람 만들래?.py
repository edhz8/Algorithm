N,H,diff = int(input()),sorted(map(int,input().split())),float('inf')
for i in range(N-3):
    for j in range(i+3, N):
        cur = H[i] + H[j]
        lo, hi = i+1, j-1
        while lo < hi:
            s = H[lo]+H[hi]
            diff = min(diff,abs(s - cur))
            if s < cur: lo += 1
            elif s > cur: hi -= 1
            else:print(0);exit(0)
print(diff)