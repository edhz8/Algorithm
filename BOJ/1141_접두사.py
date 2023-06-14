W=sorted([*open(0)][1:],key=len)
a=0
while W:w=W.pop(0)[:-1];a+=all(w!=l[:len(w)]for l in W)
print(a)