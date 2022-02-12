N,K=map(int,input().split())
arr,ans=[[0 for _ in range(6)] for _ in range(2)],0
for _ in range(N):
    a,b=map(int,input().split())
    arr[a][b-1] +=1
for i in range(2):
    for j in range(6):
        ans += arr[i][j]//K+(arr[i][j]%K!=0)
print(ans)