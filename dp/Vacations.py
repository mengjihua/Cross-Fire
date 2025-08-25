n = int(input())
lst = [0] + list(map(int, input().split()))

dp = [[float('inf')] * 3 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    op = lst[i]
    dp[i][0] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + 1
    if op == 0:
        continue
    elif op == 1:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    elif op == 2:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    else:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n][0], dp[n][1], dp[n][2]))