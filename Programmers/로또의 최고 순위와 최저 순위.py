def solution(lottos, win_nums):
    low,zero=7,0
    for num in lottos :
        if num ==0 : zero+=1
        elif num in win_nums : low-=1
    if low==7 and zero==0 : low=6
    return [(low-zero),low if low!=7 else 6]