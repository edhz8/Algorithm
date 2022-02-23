import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input()))]
R,C = max(nums),10
dp = [[1 for _ in range(C)] for _ in range(R)]
I=[[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]
for i in range(1,R):
    for j in range(10):
        dp[i][j] = sum([dp[i-1][n] for n in I[j]])
print(*[sum(dp[n-1])%1234567 for n in nums],sep='\n')