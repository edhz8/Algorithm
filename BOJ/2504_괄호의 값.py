stack,brs,ans = [],['(','[',')',']'],0
def EXIT() : print(0);exit(0)
for c in input():
    if c in brs[:2]: stack.append(c)
    else :
        me,tmp = brs.index(c),0
        while True:
            if not stack or stack[-1] == brs[(me-2)^1] : EXIT()
            pop = stack.pop()
            if isinstance(pop,int): tmp += pop
            elif pop == brs[me-2] :  
                stack.append(tmp*me if tmp!=0 else me)
                break
            else : EXIT()
for n in stack:
    if isinstance(n,int) : ans += n
    else : EXIT()
print(ans)