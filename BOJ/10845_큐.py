q=[]
for l in[*open(0)][1:]:
    if'u'in l:q.append(l[5:-1])
    else: print(len(q)if'z'in l else+(not q)if'y'in l else-1 if not q else q.pop(0) if'p'in l else q[-('k'in l)])