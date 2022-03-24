while (s:=input()) !='.':
    S,t = [],1
    for i in s:
        if i == '(' or i == '[': S.append(i)
        elif i == ')':
            if not S or S[-1] == '[': t=0;break
            elif S[-1] == '(': S.pop()
        elif i == ']':
            if not S or S[-1] == '(': t = 0;break
            elif S[-1] == '[': S.pop()
    print('yes' if t and not S else 'no')