N,B = map(int,input().split())
g = [list(map(lambda x : x%1000 , map(int,input().split()))) for _ in range(N)]
def mul(A,B): return [[sum([A[i][k]*B[k][j] for k in range(N)])%1000 for j in range(N)] for i in range(N)]
def divide(b):
    if b==1 : return g
    tmp = divide(b//2)
    return mul(mul(tmp,tmp),g) if b&1 else mul(tmp,tmp)
for i in divide(B) : print(*i)