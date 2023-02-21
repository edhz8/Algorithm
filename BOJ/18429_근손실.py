N,K=map(int,input().split())
A=[*map(int,input().split())]
V=[0]*len(A)
answer = 0
def rec(depth,cur):
    global answer
    if depth == len(A):
        answer += 1
        return
    for i in range(len(A)):
        if not V[i] and cur+A[i]-K>=500:
            V[i]=1
            rec(depth+1,cur+A[i]-K)
            V[i]=0
rec(0,500)
print(answer)
# 1157