import sys
input = sys.stdin.readline
N,M = map(int,input().split())
g,v,q,cnt=[[0 for _ in range(N+1)] for _ in range(N+1)],[0 for _ in range(N+1)],[],0
for _ in range(M):
    a,b=map(int,input().split())
    g[a][b]=g[b][a]=1
for i in range(1,N+1):
    if not v[i] :
        cnt+=1
        v[i]=i
        q.append(i)
        while q:
            n=q.pop()
            for i in range(1,N+1):
                if g[n][i] and not v[i] : 
                    q.append(i)
                    v[i]=n
print(cnt)