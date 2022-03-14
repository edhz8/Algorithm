l=[0]*9**5
f=open(0)
next(f)
for i in f:l[int(i)]+=1
for i in range(9**5):
    for j in range(l[i]):print(i)