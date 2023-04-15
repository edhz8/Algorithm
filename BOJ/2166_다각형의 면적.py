import sys
input = sys.stdin.readline
n=int(input())
P=[[*map(int,input().split())] for _ in ' '*n]
P.append(P[0])
print(round(abs((sum(P[i][0]*P[i+1][1] for i in range(n))-sum(P[i][1]*P[i+1][0] for i in range(n)))/2),1))