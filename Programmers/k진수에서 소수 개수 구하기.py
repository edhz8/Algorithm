def convert(n, k):
    T = "0123456789"
    q, r = divmod(n, k)
    return T[r] if q == 0 else convert(q, k) + T[r]
def isPrime(x):
    if x<2 : return 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return 0
    return 1
def solution(n, k):
    ans = 0
    for num in convert(n,k).split("0"):
        if not num.isdigit() : continue
        if(isPrime(int(num))) : ans +=1
    return ans