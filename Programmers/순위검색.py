from collections import defaultdict
from bisect import bisect_left
def solution(info, query):
    S,ans=defaultdict(list),[]
    for i in sorted([i.split() for i in info],key=lambda x:int(x[4])): S[tuple(i[:4])].append(int(i[-1]))
    for string in query:
        string = string.replace(' and ',' ').split()
        ans.append(sum([len(v)-bisect_left(v,int(string[-1])) for k,v in S.items() if all(zs==zk or zs=='-' for zs,zk in zip(string[:4],k))]))
    return ans