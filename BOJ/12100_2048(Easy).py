import sys
input = sys.stdin.readline
N=int(input())
G=[[*map(int,input().split())] for _ in ' '*N]
answer = 0
def getNewLine(cur) :
    cur = [c for c in cur if c>0]
    newLine=[]
    while cur:
        if len(cur)==1 : newLine.append(cur.pop())
        else :
            if cur[-1] == cur[-2] : newLine.append(cur.pop()+cur.pop())
            else : newLine.append(cur.pop())
    newLine += [0]*(N-len(newLine))
    return newLine
def rotate(g) : return [[g[i][j] for i in range(N)] for j in range(N)]
def up(g):
    newG=[]
    for cur in [[g[N-1-j][i] for j in range(N)] for i in range(N)] : newG.append(getNewLine(cur))
    return newG
def down(g):
    newG=[]
    for cur in [[g[j][i] for j in range(N)] for i in range(N)] : newG.append(getNewLine(cur))
    return newG
def left(g):
    newG=[]
    for cur in [line[::-1] for line in g]: newG.append(getNewLine(cur))
    return newG
def right(g):
    newG=[]
    for cur in [line[:] for line in g]: newG.append(getNewLine(cur))
    return newG

def rec(g,cnt):
    global answer
    answer = max(answer,max(max(line) for line in g))
    if cnt==5 : return
    rec(left(g),cnt+1)
    rec(right(g),cnt+1)
    rec(up(g),cnt+1)
    rec(down(g),cnt+1)
rec(G,0)
print(answer)