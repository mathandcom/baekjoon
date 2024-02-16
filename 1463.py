n = int(input())
# 1부터 n까지 모든 경우의 수를 계산
dp = [0] * (n+1)

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])
