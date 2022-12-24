def solution(e, starts):
    cnts = [0]*(e+1)
    for i in range(1,e+1):
        for j in range(1,e//i+1):
            cnts[i*j]+=1
    indexs=[0]*(e+1)
    index,value=-1,0
    for i in range(e,min(starts)-1,-1):
        if value<=cnts[i]: value,index=cnts[i],i
        indexs[i]=index
    return [indexs[i] for i in starts]