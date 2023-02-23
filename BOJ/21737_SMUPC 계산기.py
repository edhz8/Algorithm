N=int(input())
x,y,z=[],'',[]
answer = []
def cal(x,y,z):
    if y=='S' : return int(x)-int(z)
    if y=='M' : return int(x)*int(z)
    if y=='U' :
        if int(x)>0 : return int(x)//int(z)
        else : return -((-int(x))//int(z))
    if y=='P' : return int(x)+int(z)
for c in input():
    if c.isdigit() :
        if y: z.append(c)
        else : x.append(c)
    elif c in ['S','M','U','P'] : 
        if y : x,y,z=[str(cal(''.join(x),y,''.join(z)))],c,[]
        else : y=c
    else : 
        if y : x,y,z=[str(cal(''.join(x),y,''.join(z)))],'',[]
        answer.append(''.join(x))
if answer : print(*map(int,answer))
else: print('NO OUTPUT')