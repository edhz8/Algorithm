for l in [*open(0)][:-1]:
    a,b,c=l.split()
    print(a,'Senior'if int(b)>17 or int(c)>79 else 'Junior')