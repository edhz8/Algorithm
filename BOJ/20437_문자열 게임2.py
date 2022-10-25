I=input
for _ in ' '*int(I()):
    d,W,K,T,F = {},I(),int(I()),10001,0
    for i,w in enumerate(W):
        if w in d:d[w]+=[i]
        else:d[w]=[i]
        if len(d[w])==K:L=d[w][-1]-d[w].pop(0);T,F = min(T,L),max(F,L)
    if T==10001 and F==0:print(-1)
    else:print(T+1,F+1)