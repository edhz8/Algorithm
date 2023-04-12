import sys
input = sys.stdin.readline
N,C=map(int,input().split())
X=sorted([int(input()) for _ in ' '*N])
Min,Max,answer=1,(X[N-1]-X[0])//(C-1)+1,0
while Min<=Max:
    Mid = (Min+Max)//2
    cnt,cur=1,X[0]
    for i in range(1,N):
        if X[i]-cur >= Mid : cnt+=1;cur=X[i]
    if cnt>=C : 
        answer = Mid
        Min = Mid+1
    else : Max = Mid-1
print(answer)