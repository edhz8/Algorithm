s=open(0).read().split()
for j in range(15):
    for i in range(5):
        if len(s[i])>j : print(s[i][j],end='')