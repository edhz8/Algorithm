def solution(new_id):
    t=[]
    for s in new_id.lower():
        if s.isalpha() or s.isdigit() or s in ['-','_','.'] : t.append(s)
    prev,new_id='',[]
    for s in t:
        if s=='.' and prev=='.' : continue
        else : new_id.append(s);prev=s
    for i in [0,-1] :
        if new_id and new_id[i]=='.' : new_id.pop(i)
    if not new_id : new_id.append('a')
    if len(new_id)>=16 : new_id=new_id[:14+int(new_id[14]!='.')]
    return ''.join(new_id) + (new_id[-1]*(3-len(new_id)) if len(new_id)<=2 else '')