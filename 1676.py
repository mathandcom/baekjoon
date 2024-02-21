n = int(input())
ans = 0
for i in range(2,n+1):
    while i != 1:
        if i % 5 == 0:
            ans += 1
            i = i // 5
        else:
            i = 1
print(ans)
