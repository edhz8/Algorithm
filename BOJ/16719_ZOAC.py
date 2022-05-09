a=[]
def rec(s):
    if not s : return
    a.insert(0,s)
    rec(min(s[:i]+s[i+1:] for i in range(len(s))))
rec(input())
print(*a)