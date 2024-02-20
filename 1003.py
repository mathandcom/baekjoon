t = int(input())
anslist = []

for i in range(t):
    n = int(input())
    dp = [[0,0]] * (n + 1)
    for j in range(n+1):
        if j == 0:
            dp[0] = [1,0]
        elif j == 1:
            dp[1] = [0,1]
        else:
            dp[j] = [dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]]
    ans = dp[n]
    anslist.append(ans)
for ans in anslist:
    print(ans[0],ans[1])
