v=set()
def d(num):
    if num>10000 or num in v: return
    v.add(num)
    d(eval(f"{num}+{'+'.join(str(num))}"))
for i in range(1,10000): 
    if i not in v: print(i);d(i)