A,B,C,D=zip(*[[*map(int,o.split())]for o in[*open(0)][1:]])
E={}
for a in A:
    for b in B:E[a+b]=E.get(a+b,0)+1
print(sum(E.get(-c-d,0)for c in C for d in D))