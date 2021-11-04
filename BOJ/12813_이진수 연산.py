a,b=int(input(),2),int(input(),2)
n=100000
m=2**n-1
print(*[bin(N)[2:].zfill(n) for N in [a&b,a|b,a^b,a^m,b^m]],sep='\n')