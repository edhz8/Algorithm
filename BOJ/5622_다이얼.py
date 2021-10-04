r=0
for c in input():
    if c<'D':r+=3
    elif c<'G':r+=4
    elif c<'J':r+=5
    elif c<'M':r+=6
    elif c<'P':r+=7
    elif c<'T':r+=8
    elif c<'W':r+=9
    else:r+=10
print(r)