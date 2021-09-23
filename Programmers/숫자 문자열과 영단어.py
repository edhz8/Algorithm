def solution(s):
    n=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10): s = s.replace(n[i],str(i))
    return int(s)