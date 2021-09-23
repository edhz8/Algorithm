def solution(answers):
    score,ans,p = [[4,0],[1,0],[2,0],[3,0]],[],[[],[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i in range(len(answers)):
        for j in range(1,4): score[j][1] -= int(p[j][i%len(p[j])] == answers[i])
    score.sort(key = lambda x : (x[1],x[0]))
    for i in score :
        if i[1] == score[0][1] : ans.append(i[0])
        else : break
    return ans