stack=[]
pair={')':'(',']':'['}
value={')':2,']':3}
for c in input():
    if c in pair:
        if not stack:print(0);exit(0)
        num=0
        while (poped:=stack.pop())!=pair[c]: 
            if (not stack) or isinstance(poped,str): print(0);exit(0)
            else: num+=poped
        stack.append(value[c]*num if num else value[c])
    else : stack.append(c)
answer = 0
for c in stack:
    if isinstance(c,int):answer+=c
    else:print(0);exit(0)
print(answer)