N,M=map(int,input().split())
print([[M-2,min(M,4)][M<7],[(min(M,7)-1)//2+1,1][N%2]][N<3])