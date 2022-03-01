N,K=map(int,input().split())
if N==K :
    print(0,1,sep='\n')
    exit(0)
q=[(N,0)]
cnt = 0
L = 100001
dp,dp[N] = [float('inf') for _ in range(L)],0
while q:
    num,time  = q.pop(0)
    for node in [num*2,num+1,num-1]:
        if 0<=node<L and dp[node] >=time+1 and time+1<=dp[K]:
            dp[node] = time+1
            if node == K : cnt +=1
            q.append((node,time+1))
print(dp[K],cnt,sep='\n')