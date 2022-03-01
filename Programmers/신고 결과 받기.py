from collections import defaultdict
def solution(id_list, report, k):
    cnts = defaultdict(int)
    rlist = defaultdict(list)
    for s in report:
        a,b=s.split()
        if b in rlist[a] : continue
        if cnts[b]>-1:cnts[b] += 1
        rlist[a].append(b)
        if cnts[b]>=k : cnts[b] = -1
    ans = []
    for name in id_list:
        count = 0
        for n in rlist[name]:
            if cnts[n] == -1 : count+=1
        ans.append(count)
    return ans