r=range
G=[l.replace('.','D')for l in[*open(0)][1:]]
R,C=len(G),len(G[0])
print(+all(G[x][y]!='W'or'S'!=G[x+c][y+d]for x in r(R)for y in r(C)for c,d in[(-1,0),(0,1),(1,0),(0,-1)]if 0<=x+c<R and 0<=y+d<C),*G)