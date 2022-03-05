def getMask(g):
    ret = 0
    for i in range(4):
        for j in range(4):
            if g[i][j]==1 : ret |= (1<<(i*4+j))
    return str(bin(ret))[::-1][:-2]
def setGrid(g,n):
    for i in range(len(n)):
        g[i//4][i%4] = 1 if n[i]=='1' else 2
    for i in range(len(n),16):
        g[i//4][i%4] = 2
def turni(n,i):
    n = list(n)
    tmp = n[i*4]
    for k in range(1,4): n[i*4 + (k-1)] = n[i*4 + k]
    n[i*4+3] = tmp
    return str(n)
def turnj(n,j):
    n = list(n)
    tmp = n[j]
    for k in range(1,4): n[j + (k-1)*4] = n[j + k*4]
    n[j+12] = tmp
    return str(n)
def isOver(n,end):
    return n == end
def solution(grid):
    q = [(getMask(grid),0)]
    end = getMask([[1,1,2,2],[1,1,2,2],[2,2,1,1],[2,2,1,1]])
    while q:
        mask,cnt = q.pop(0)
        for i in range(4):
            tmp = turni(mask,i)
            if isOver(tmp,end) : 
                return cnt+1
                break
            else : q.append((tmp,cnt+1))
            tmp = turnj(mask,i)
            if isOver(tmp,end) : 
                return cnt+1
                break
            else : q.append((getMask(tmp),cnt+1))