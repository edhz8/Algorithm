L,C=map(int,input().split())
chars=sorted(input().split())
S=['']*L
def rec(start,cur):
    global S
    if cur==L:
        ja=sum(c in'aeiou'for c in S)
        if ja>0 and L-ja>1 : print(''.join(S))
        return
    for i in range(start,C):S[cur]=chars[i];rec(i+1,cur+1)
rec(0,0)