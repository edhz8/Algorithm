import sys
input = sys.stdin.readline
n = int(input())
graph = [[0]]+[[0] + list(map(int, input().split())) for _ in range(n)]
total = sum(sum(g) for g in graph)
ans = float('inf')

def solve(x, y, d1, d2):
    global ans
    line = set()
    MIN,MAX,TOTAL=float('inf'),-float('inf'),total
    for i in range(d1+1): 
        line.add((x+i,y-i))
        line.add((x+d2+i,y+d2-i))
    for i in range(d2+1): 
        line.add((x+i,y+i))
        line.add((x+d1+i,y-d1+i))

    tmp = 0
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if (i,j) in line: break
            tmp += graph[i][j]
    MIN,MAX=min(MIN,tmp),max(MAX,tmp)
    TOTAL -= tmp

    tmp = 0
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if (i,j) in line: break
            tmp += graph[i][j]
    MIN,MAX=min(MIN,tmp),max(MAX,tmp)
    TOTAL -= tmp
    
    tmp = 0
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if (i,j) in line: break
            tmp += graph[i][j]
    MIN,MAX=min(MIN,tmp),max(MAX,tmp)
    TOTAL -= tmp
    
    tmp = 0
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if (i,j) in line: break
            tmp += graph[i][j]
    MIN,MAX=min(MIN,tmp),max(MAX,tmp)
    TOTAL -= tmp
    
    MIN,MAX=min(MIN,TOTAL),max(MAX,TOTAL)
    ans = min(ans, MAX-MIN)

for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x+d1+d2>n or y-d1<1 or y+d2>n: continue
                solve(x, y, d1, d2)

print(ans)