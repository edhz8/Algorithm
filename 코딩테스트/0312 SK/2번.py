def solution(n, clockwise):
    g = [[0 for _ in range(n)]for _ in range(n)]
    start,end = 1,n-1
    for i in range(n//2):
        nums = [start] + list(range(start+1,end+1))[::1 if clockwise else -1]
        for x in range(len(nums)): g[i][x+i] = g[x+i][n-1-i] = g[n-1-i][n-1-x-i] = g[n-1-x-i][i] = nums[x]
        start,end = end+1,end+(end-start-1)
    if n%2==1 : g[n//2][n//2] = start
    return g