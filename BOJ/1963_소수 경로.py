import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
isPrime=[1 for _ in range(10000)]
for i in range(2, 100):
        if isPrime[i]:
            for j in range(2*i, 10000, i): isPrime[j] = 0
for _ in range(int(input())):
    num,dst = map(int,input().split())
    q=[(num,0)]
    visited = [0 for _ in range(10000)]
    visited[num] = 1
    while q:
        n,c=q.pop(0)
        if n == dst : 
            print(c)
            break
        snum = str(n)
        for i in range(4):
            for j in range(10) :
                tnum = int(snum[:i]+str(j)+snum[i+1:])
                if tnum == num or (i==0 and j==0) : continue
                if visited[tnum]==0 and isPrime[tnum] : 
                    q.append((tnum,c+1))
                    visited[tnum] = 1