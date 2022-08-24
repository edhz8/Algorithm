def solution(X, Y):
    nx,ny = [0]*10,[0]*10
    for x in X: nx[int(x)]+=1
    for y in Y: ny[int(y)]+=1
    ret = ''
    for n in range(9,-1,-1): 
        if nx[n] and ny[n] : ret += str(n)*min(nx[n],ny[n])
    if ret and ret[0] == '0' : ret = '0'
    return ret if ret else '-1'