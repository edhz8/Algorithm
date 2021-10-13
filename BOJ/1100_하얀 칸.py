ans = 0
for i in range(8):
    t=input()
    for j in range(8):
        if i%2 == j%2 and t[j]=='F' : ans+=1
print(ans)