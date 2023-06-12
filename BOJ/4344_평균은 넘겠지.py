for _ in ' '*int(input()):
    N,*nums = map(int,input().split())
    mean = sum(nums)/N
    cnt=0
    for n in nums :
        if n > mean : cnt += 1
    print(f'{cnt*100/N:.3f}%')