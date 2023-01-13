N=int(input())
S=list(input())
nums=[int(input()) for _ in ' '*N]
q=[]
for i in range(len(S)):
    cur = S[i]
    if cur in '+-*/': 
        b,a=q.pop(),q.pop()
        q.append(eval(str(a)+cur+str(b)))
    else: q.append(nums[ord(cur)-65])
print("%0.2f"%q[0])
# 10:35(21분 소요)