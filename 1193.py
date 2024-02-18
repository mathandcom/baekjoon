n = int(input())
i = 1

while n > i:
    n -= i
    i += 1
j = n

if i % 2 == 0:
    up = j
    down = i + 1 - j
else:

    up = i + 1 - j
    down = j
print(str(up) + "/" + str(down))
