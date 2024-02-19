key = input()
keylist= list(key)
indlist = []
for i in range(len(keylist)):
    indlist.append((i,keylist[i]))
newindlist = sorted(indlist, key = lambda x : x[1])
leng = len(keylist)

crypto = input()
crypto = list(crypto)
num = len(crypto) // leng
newlist = []
for i in range(leng):
    newlist.append(crypto[num*i:num*(i+1)])
anslist = [[]*i for i in range(leng)]
for i in range(len(newindlist)):
    anslist[newindlist[i][0]] = newlist[i]
fans = [[]*i for i in range(len(anslist[0]))]
for ans in anslist:
    for i in range(len(ans)):
        fans[i].append(ans[i])
result = ''
for f in fans:
    result += ''.join(z for z in f)
print(result)
