from collections import defaultdict
def solution(clothes):
    ret = 1
    cloth = defaultdict(int)
    for x,y in clothes: cloth[y]+=1
    for t,l in cloth.items(): ret*=(l+1)
    return ret-1