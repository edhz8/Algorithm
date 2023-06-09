S,_,*L=open(0)
G=[[0]*26]
O=lambda c:ord(c)-97
for c in S[:-1]:G+=[G[-1][:]];G[-1][O(c)]+=1
for s in L:c,l,h=s.split();print(G[int(h)+1][O(c)]-G[int(l)][O(c)])