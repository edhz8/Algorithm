from collections import deque
def solution(begin, target, words):
    if target not in words : return 0
    q=deque([begin])
    v,v[begin]={w:0 for w in words},0
    while q:
        cur = q.popleft()
        if cur==target : print(v);return v[target]
        for w in words:
            if v[w]==0 and sum([1 for a,b in zip(cur,w) if a!=b])==1 :
                v[w] = v[cur]+1
                q.append(w)