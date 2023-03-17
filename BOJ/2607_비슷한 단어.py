import sys
from collections import defaultdict
input = sys.stdin.readline
N=int(input())
W=defaultdict(int)
for c in input().rstrip() : W[c] += 1
answer = 0
for _ in ' '*(N-1):
    word=defaultdict(int)
    for c in input().rstrip() : word[c] += 1
    plus=0
    minus=0
    cnt_p=0
    cnt_m=0
    for key in W.keys() : word[key] -= W[key]
    for v in word.values() :
        if v>0 : plus +=v;cnt_p+=1
        if v<0 : minus +=-v;cnt_m+=1
    if plus<2 and minus<2 and cnt_p<2 and cnt_m<2: answer +=1
print(answer)