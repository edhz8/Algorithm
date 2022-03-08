import sys
from collections import defaultdict
input = sys.stdin.readline
def convert(str):
    h,m=str.split(':')
    return h*60 + m
S,E,Q=map(convert,input().strip().split())
enter,out = defaultdict(bool),defaultdict(bool)
while True:
    try:
        time,nick=input().strip().split()
        time = convert(time)
        if time<=S : enter[nick] = True
        elif E<=time<=Q : out[nick] = True
    except : break
print(sum([enter[nick] and out[nick] for nick in enter.keys()]))