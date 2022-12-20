def solution(n, stations, w):
    start = 1
    ans = 0
    l = 2*w+1
    for station in stations:
        cnt = station-w-start
        ans += (cnt//l +(cnt%l!=0))
        start = station+w+1
    if start<=n:
        cnt = n-start+1
        ans += (cnt//l +(cnt%l!=0))
    return ans