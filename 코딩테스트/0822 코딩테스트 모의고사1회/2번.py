def solution(want, number, discount):
    cnt,nums,ret=dict(),dict(),0
    for w,n in zip(want,number) : 
        nums[w]=n
        cnt[w]=0
    for d in discount[:10] : 
        if d in want : cnt[d] +=1
    if cnt == nums : ret +=1
    for p,d in zip(discount[:len(discount)-10],discount[10:]) :
        if p in want : cnt[p] -=1
        if d in want : cnt[d] +=1
        if cnt == nums : ret +=1
    return ret