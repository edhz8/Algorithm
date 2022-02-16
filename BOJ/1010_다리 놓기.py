from math import factorial
for i in range(int(input())):
    ans = 0
    N,M=map(int,input().split())
    print(factorial(M)//(factorial(M-N)*factorial(N)))