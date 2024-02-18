n = int(input())
whitelist = [[ 0 for i in range(100)]for i in range(100)]
pointlist = []
for i in range(n):
    point = tuple(map(int, input().split()))
    pointlist.append(point)
for point in pointlist:
    for i in range(10):
        for j in range(10):
            whitelist[point[0]+i][point[1]+j] = 1
ans = 0
for black in whitelist:
    ans += sum(black)
print(ans)
