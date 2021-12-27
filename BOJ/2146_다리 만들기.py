from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find_island(i,j,k):
    global ans
    Q = deque()
    Q.append((i,j))
    Q2 = deque()
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if nr>N-1 or nc>N-1 or nr<0 or nc<0 or arr[nr][nc]==k:continue
            if not arr[nr][nc]:
                Q2.append((nr,nc,1))
                continue
            arr[nr][nc] = k
            Q.append((nr,nc))
    def bridge(n):
        nonlocal Q2
        while Q2:
            r, c, dis = Q2.popleft()
            if dis>=ans:
                return ans
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr > N - 1 or nc > N - 1 or nr < 0 or nc < 0 or arr[nr][nc] == n or visit[nr][nc]:continue
                if not arr[nr][nc]:
                    Q2.append((nr, nc, dis+1))
                    visit[nr][nc] = 1
                elif arr[nr][nc]:
                    return dis
        return ans

    distance = bridge(k)
    if ans>distance:
        ans = distance

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
n_island = 1
ans = 100**2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            n_island += 1
            arr[i][j] = n_island
            find_island(i,j,n_island)
print(ans)