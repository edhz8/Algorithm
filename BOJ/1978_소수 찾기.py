def isPrime(x):
    if x== 1 : return 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
input()
print(sum([isPrime(i) for i in map(int,input().split())])) 