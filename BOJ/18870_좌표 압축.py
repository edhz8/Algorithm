import sys 
input = sys.stdin.readline
N = int(input()) 
l = list(map(int,input().split())) 
l2 = list(sorted(set(l))) 
dic = {l2[i]:i for i in range (len(l2))} 
print(*[dic[n] for n in l])