o=int(input())
for n in map(abs,range(1-o,o)):print(" "*(o-n-1)+"*"*(n*2+1))