N,r,c = map(int, input().split())
ans = 0
while N != 0:
    N -= 1
    tn=2**N
    if r<tn and c<tn : ans += tn*tn*0
    elif r < tn and c >= tn: 
        ans += tn*tn
        c -= tn 
    elif r >= tn and c < tn: 
        ans += tn*tn*2
        r -= tn 
    else:
        ans += tn*tn*3
        r -= tn
        c -= tn
print(ans)