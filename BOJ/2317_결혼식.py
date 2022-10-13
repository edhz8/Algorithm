import sys
input = sys.stdin.readline
N,K=map(int,input().split())
S=[int(input()) for _ in ' '*K]
for n in sorted([int(input()) for _ in ' '*(N-K)]):
    MIN=float('inf')
    index=-1
    for i in range(len(S)+1):
        cur = (abs(S[i-1]-n) if i!=0 else 0)+(abs(S[i]-n) if i!=len(S) else 0)
        if cur<MIN :
            index=i
            MIN=cur
        print(n,i,cur)
    S.insert(index,n)
    print(S,MIN,index)