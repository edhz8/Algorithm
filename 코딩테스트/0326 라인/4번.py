def solution(arr, brr):
    cnt = 0
    for i in range(1,len(arr)):
        cha = arr[i-1] - brr[i-1]
        if cha == 0 : continue
        arr[i-1] -= cha
        arr[i] += cha
        cnt +=1
    return cnt