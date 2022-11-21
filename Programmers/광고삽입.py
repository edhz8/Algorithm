def parseTime(time):
    H,M,S=map(int,time.split(':'))
    return (H*60+M)*60+S

def toStr(time):return ':'.join([str(time // 3600).zfill(2),str(time % 3600 // 60).zfill(2),str(time % 3600 % 60).zfill(2)])

def solution(play_time, adv_time, logs):
    dp = [0] * (parseTime(play_time) + 1)
    MAX,ans = -1,0    
    for log in logs:
        start,end=map(parseTime,log.split('-'))
        dp[start] += 1
        dp[end] -= 1
        
    for i in range(1, parseTime(play_time)):dp[i]+=dp[i-1]
    for i in range(1, parseTime(play_time)):dp[i]+=dp[i-1]

    for i in range(parseTime(adv_time)-1, parseTime(play_time)):
        head= i-parseTime(adv_time)
        temp = dp[i] - dp[head] 
        if temp > MAX:
            MAX = temp
            ans = head + 1
    return toStr(ans)