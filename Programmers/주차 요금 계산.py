from collections import defaultdict
from math import ceil
def convert(string):
    h,m = map(int,string.split(':'))
    return h*60+m
def solution(fees, records):
    ans = []
    sums = defaultdict(int)
    cur = defaultdict(int)
    for line in records:
        time,num,cmd = line.split()
        if cmd == 'IN':
            cur[num] = convert(time) if time!='00:00' else -1
        else : 
            sums[num] += (convert(time) - cur[num]) if cur[num] != -1 else convert(time)
            cur[num] = 0
    for num in cur.keys():
        if cur[num] : sums[num] += (1439-cur[num]) if cur[num] != -1 else 1439
    gt,gf,dt,df=fees
    for num in sorted(cur):
        time = sums[num]
        ans.append(gf if time<=gt else gf + ceil((time-gt)/dt)*df)
    return ans