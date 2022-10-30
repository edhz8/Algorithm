from re import compile
cur,total,history=[],[],set()
def cnt(index):
    if index==len(total):
        s=frozenset(cur)
        if s not in history : history.add(s)
        return
    for i in total[index]:
        if i not in cur:
            cur.append(i)
            cnt(index+1)
            cur.pop()
def solution(user_id, banned_id):
    global total
    for b in banned_id:
        bc = compile(b.replace('*','.'))
        total.append([i for i,u in enumerate(user_id) if bc.match(u) and len(b)==len(u)])
    cnt(0)
    return len(history)