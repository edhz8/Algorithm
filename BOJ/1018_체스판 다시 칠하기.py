N,M=map(int,input().split())
g,MIN=[input() for _ in range(N)],64
for i in range(N-7):
    for j in range(M-7):
        s,c=g[i][j],0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if ((i+j)%2!=(x+y)%2 and s==g[x][y]) or ((i+j)%2==(x+y)%2 and s!=g[x][y]): c+=1
        MIN = min(MIN,c if c<32 else 64-c)
print(MIN)