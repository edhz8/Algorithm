N,sik = int(input()),input()
num,op=list(sik[0::2]),list(sik[1::2])
print(num,op)
MAX = -float('inf')
def rec(i) :
    global MAX
    if len(op)<=i : 
        cur=num[0]
        for R,O in zip(num[1:],op): cur = eval(str(cur)+O+R)
        MAX = max(MAX,int(cur))
        return
    l,r,o=num[i],num.pop(i+1),op.pop(i)
    num[i]=str(eval(l+o+r))
    rec(i+1)
    num[i]=l
    num.insert(i+1,r)
    op.insert(i,o)
    rec(i+1)
rec(0)
print(MAX)