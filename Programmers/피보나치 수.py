def solution(n):
    a,b = 0,1
    if n<2 : return n
    for i in range(2,n+1): b,a=a+b,b
    return b%1234567