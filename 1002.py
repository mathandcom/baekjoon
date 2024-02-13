T = int(input())
anslist= []
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ans = 0
    
    xr = abs(x1 - x2)
    yr = abs(y1 - y2)
    
    r = (xr ** 2 + yr ** 2)**(1/2)
    if r == 0:
        if  r1 == r2:
            ans = -1
        else:
            ans = 0
    elif r > r1 + r2:
        ans = 0
    elif abs(r1 - r2) < r < r1 + r2:
        ans = 2
    elif r == r1 + r2 or r == abs(r1 - r2):
        ans = 1
        
    
    anslist.append(ans)
for ans in anslist:
    print(ans)
