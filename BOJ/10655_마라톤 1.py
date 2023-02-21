N=int(input())
dp = [0]*(N+1)
P=[]
Max,index,answer=0,0,0
for i in range(N):
    if i==0 : P.append([*map(int,input().split())])
    else :
        x,y=map(int,input().split())
        px,py=P[-1]
        dp[i] = abs(px-x) + abs(py-y)
        P.append([x,y])
    if i>=2:
        x,y=P[-1]
        px,py=P[-3]
        Max = max(Max,dp[i-1]+dp[i]-(abs(px-x)+abs(py-y)))
    answer += dp[i]
print(answer-Max)