def num(n) : return ((n-1)%4)+1
def move(f,t) :
    if f==0 : return 2
    if f==t : return 1
    if t in [num(f-1),num(f+1)] : return 3
    if t == num(f+2) : return 4
l,r,answer=0,0,0
for t in map(int,input().split()) :
    if t==0 : break
    lp,rp=move(l,t),move(r,t)
    if lp>rp :
        r=t
        answer += rp
    else :
        l=t
        answer += lp
print(answer)