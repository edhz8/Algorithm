dp=[set() for _ in range(51)]
for _ in range(int(input())):
    i=input()
    dp[len(i)].add(i)
for i in range(51):dp[i] and print(*sorted(dp[i]),sep='\n')