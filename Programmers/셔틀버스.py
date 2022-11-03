from heapq import heapify,heappop
def tom(time):
    h,m=map(int,time.split(':'))
    return h*60+m
def ret(num):return ':'.join(map(pad,divmod(num,60)))
def pad(num): return '0'+str(num) if num<10 else str(num)
def solution(n, t, m, timetable):
    times=[tom(time) for time in timetable];heapify(times)
    cur=tom('09:00')
    for i in range(n):
        for j in range(m):
            if not times: return ret(cur)
            if i==n-1 and j==m-1 :
                if times[0]>cur : return ret(cur)
                elif times[0]==cur : return ret(cur-1)
                elif times[0]<cur : return ret(times[0]-1) 
            if times[0]<=cur : heappop(times)
        cur+=t