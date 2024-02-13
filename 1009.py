#1009번 재귀함수이용 풀이
T = int(input())

def checkfirst(a,b,n):
    b = b*a
    if b % 10 == a % 10:
        return n
    else:
        n = n + 1
        return checkfirst(a,b,n)
anslist=[]
for i in range(T):
    a, b = map(int, input().split())
    n = checkfirst(a,a,1)
    c = b % n
    if c == 0:
        ans = (a**n) % 10
    else:
        ans = (a ** c) % 10
    if ans == 0:
        ans = 10
    anslist.append(ans)
for ans in anslist:
    print(ans)
