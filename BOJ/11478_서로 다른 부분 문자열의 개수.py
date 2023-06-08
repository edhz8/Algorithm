s=input()
r=range(1000)
print(len({s[i:j+1]for i in r for j in r})-1)