N,primes = int(input()),[]
def isPrime(x):
    if x<2 : return 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
def rec(length,num):
    if length == N:
        primes.append(num)
        return
    num *= 10
    for i in range(10):
        tnum = num+i
        if isPrime(tnum): rec(length+1,tnum)
rec(0,0)
print(*primes,sep='\n')