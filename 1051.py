def checkrow(a,numlist):
    indlist = []
    for i in range(len(numlist)):
        if numlist[i] == a:
            indlist.append(i)
    if len(indlist) > 1:
        return indlist
    else:
        return 0

def checkrec(row,indlist,numlist):
    num = numlist[row][indlist[0]]
    maxans = 1
    for i in range(1,len(indlist)):
        for j in range(i):
            dif = indlist[i] - indlist[j]            
            if len(numlist) > row + dif:
                if numlist[row+dif][indlist[i]] == num and numlist[row+dif][indlist[j]] == num:
                    ans = (indlist[i] - indlist[j] + 1) ** 2
                    if ans > maxans:
                        maxans = ans
    return maxans
N, M = map(int, input().split())
numlist = []
for i in range(N):
    num = list(map(int, str(input())))
    numlist.append(num)
maxans = 1
row = 0    
for num in numlist:
    for i in range(len(num)):
        a = int(num[i])
        if checkrow(a,num):
            ans = checkrec(row, checkrow(a,num), numlist)
            if ans > maxans:
                maxans = ans

    row +=1

print(maxans)
