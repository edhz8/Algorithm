q,cs,T=[],list(input()),isinstance
while cs:
    c=cs.pop(0)
    if c.isdigit()or c=='(':q.append(c)
    else:
        S=0
        while(n:=q.pop())!='(':S+=(n if T(n,int) else 1)
        q.append(S*int(q.pop()))
print(sum(n if T(n,int) else len(n) for n in q))