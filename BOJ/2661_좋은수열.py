N=int(input())
def R(S):
    if len(S)==N:print(S);exit()
    [R(s)for s in[S+c for c in'123']if all(s[-i:]!=s[-2*i:-i]for i in range(1,len(s)//2+1))]
R('')