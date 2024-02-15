import math
def func1072(x,y):
    z = (y * 100) // x
    if z >= 99:
        return -1
    ans = math.ceil((x * (z+1) - 100 * y) / (99 - z))
    return ans

x, y = map(int, input().split())
print(func1072(x, y))
