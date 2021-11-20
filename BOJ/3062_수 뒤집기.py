for _ in range(int(input())):
    n=input()
    num = str(int(n) + int(n[::-1]))
    print('YES' if num == num[::-1] else 'NO') 