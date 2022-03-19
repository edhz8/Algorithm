def solution(goods):
    L = len(goods)
    result,lresult = [{} for _ in range(L)],[50 for _ in range(L)]
    for i in range(L):
        good = goods[i]
        for P in [good[j:k] for j in range(len(good)) for k in range(j+1,len(good)+1)]:
                if lresult[i] < len(P) : continue
                TRUE = True
                for l in range(L):
                    if i!=l and P in goods[l] : TRUE = False;break
                if TRUE : 
                    if lresult[i] == len(P) : result[i].add(P)
                    else : lresult[i],result[i] = len(P),{P}
    return [' '.join(sorted(i)) if i else "None" for i in result]