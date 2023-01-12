king,dol,N=input().split()
D = { 'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1] }
Kx,Ky,Dx,Dy=ord(king[0])-65,int(king[1])-1,ord(dol[0])-65,int(dol[1])-1
for _ in ' '*int(N):
    dx,dy=D[input()]
    nkx,nky=Kx+dx,Ky+dy
    ndx,ndy=Dx+dx,Dy+dy
    if 0<=nkx<8 and 0<=nky<8: 
        if nkx==Dx and nky==Dy:
            if 0<=ndx<8 and 0<=ndy<8 : Kx,Ky,Dx,Dy=nkx,nky,ndx,ndy
        else : Kx,Ky=nkx,nky
print(chr(Kx+65)+str(Ky+1),chr(Dx+65)+str(Dy+1),sep='\n')