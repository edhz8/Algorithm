def convert(string):
    _,m,d=map(int,string.split('/'))
    ret = d
    for i in range(1,m+1):
        if i-1 in [1,3,5,7,8,10,12] : ret += 31
        elif i-1 in [4,6,9,11] : ret += 30
        elif i-1 in [2] : ret += 28
    return ret
def solution(purchase):
    day = [0 for _ in range(366)]
    for line in purchase:
        date,money  = line.split()
        date, money = convert(date),int(money)
        for i in range(date,date+30):
            if i>365 : break
            day[i] += money
    answer = [0,0,0,0,0]
    for i in range(1,366):
        if 0<= day[i] <10000 : answer[0] +=1
        elif 10000<= day[i] <20000 : answer[1] +=1
        elif 20000<= day[i] <50000 : answer[2] +=1
        elif 50000<= day[i] <100000 : answer[3] +=1
        elif 100000<= day[i] : answer[4] +=1
    return answer
print(solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]))