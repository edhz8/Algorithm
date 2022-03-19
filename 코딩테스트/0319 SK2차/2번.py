def solution(arr, processes):
    tmp = []
    for i in processes: tmp.append([int(j) if j.isdigit() else j[0] for j in i.split()])
    processes = tmp
    cur,pen,result = [],[],[]
    sec,last = 0,0
    while processes or cur or pen:
        i=0
        while i<len(cur): 
            if cur[i][2]==0 : 
                if cur[i][0]=='r' : result.append((cur[i][1],"".join(map(str,arr[cur[i][3]:cur[i][4]+1]))))
                else :
                    for j in range(cur[i][3],cur[i][4]+1): arr[j] = cur[i][5]
                cur.pop(i)
            else : i+=1
        if processes and int(processes[0][1]) == sec : pen.append(processes.pop(0))
        pen.sort(key=lambda x : -ord(x[0]))
        while True:
            if cur and pen :
                if cur[0][0]=='r' and pen[0][0] == 'r' : cur.append(pen.pop(0))
                else : break
            elif pen : cur.append(pen.pop(0))
            else : break
        for i in range(len(cur)): cur[i][2]-=1
        if cur : last +=1
        #print(sec,cur,pen)
        sec += 1
    return [i[1] for i in sorted(result)]+[str(last)]
#print(solution(["1","2","4","3","3","4","1","5"],["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))