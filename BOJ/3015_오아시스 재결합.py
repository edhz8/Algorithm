S,R=[],0
for o in map(int,[*open(0)][1:]):
    while S and S[-1][0]<o:R+=S.pop()[1]
    if not S:S+=[(o,1)]
    elif S[-1][0]==o:c=S.pop()[1];R+=c+(1^(not S));S+=[(o,c+1)]
    else:S+=[(o,1)];R+=1
print(R)