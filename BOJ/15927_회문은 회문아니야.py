def p(s,c):
    if not s : return
    if s!=s[::-1] : print(len(s));exit(0)
    else :p(s[1:] if c else s[:-1],c)
S=input()
if len(S) == S.count(S[0]) : print(-1)
else :
    p(S,1)
    p(S,0)