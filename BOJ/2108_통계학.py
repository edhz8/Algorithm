import collections as c
N,*n=map(int,open(0))
n.sort()
m=c.Counter(n).most_common(2)
print(round(sum(n)/N),n[N//2],m[-(m[0][1]==m[-1][1])][0],n[-1]-n[0])