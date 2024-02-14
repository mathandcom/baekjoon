# 점이 원 안에 있는 경우 숫자 1을 증가한다.
def checkincir(point, circle):
    xr = abs(point[0] - circle[0])
    yr = abs(point[1] - circle[1])
    r = (xr ** 2 + yr ** 2) ** (1/2)
    if circle[2] > r:
        return 1
    else:
        return 0
T = int(input())
anslist = []
for _ in range(T):
    point = list(map(int, input().split()))
    pointlist = [(point[0], point[1]),(point[2], point[3])]
    n = int(input())
    circlelist = []
    ans = 0
    for _ in range(n):
        circle = tuple(map(int, input().split()))
        circlelist.append(circle)
    for circle in circlelist:
        if checkincir(pointlist[0],circle) == 1 or checkincir(pointlist[1], circle) == 1:
            if not (checkincir(pointlist[0],circle) == 1 and checkincir(pointlist[1], circle) == 1):
                ans += 1
    anslist.append(ans)

for ans in anslist:
    print(ans)
