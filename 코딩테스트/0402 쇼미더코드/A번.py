#1차제출 : 14:36 / 2656ms / 844B
import sys
input = sys.stdin.readline
N,yaks = int(input()),list(map(int,input().split()))
hals,v,ans = [[] for _ in range(N)],[0 for _ in range(N)],float('inf')
for i in range(N): 
    for j in range(int(input())): hals[i].append(list(map(int,input().split())))

def rec(index,money):
    global ans
    money += yaks[index]
    tmp = []
    for a,d in hals[index]:
        a-=1
        tmp.append((a,yaks[a]))
        yaks[a] = 1 if yaks[a]-d<1 else yaks[a]-d
    NOT_VISITED = True
    for i in range(N):
        if not v[i] :
            NOT_VISITED = False 
            v[i] = 1
            rec(i,money)
            v[i] = 0
    for a,d in tmp:yaks[a] = d
    if NOT_VISITED : ans = min(ans,money)
for i in range(N):
    v[i] = 1
    rec(i,0)
    v[i] = 0
print(ans)