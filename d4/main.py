#list<int>
#list:
#    dic<num, (x, y, bool)>
#

file = open('inputs')

line = file.readline()

lst = map(int, line.replace('\n', '').split(','))

line = file.readline()
line = file.readline()

matrixs = []
mtx = []
x = 0
while line:
    #print(line)
    if line.lstrip().rstrip() == "":
        matrixs.append(list(mtx))
        mtx.clear()
        x = 0
    else:
        mtx.append(list(map(int , filter(bool, line.replace('\n', '').split(' ')))))

    line = file.readline()
file.close()

matrixs.append(mtx)

bk = False
resultMtx = [[]]
finalNum = 0

totalMtx = len(matrixs)
winMtx = set()

for l in lst:
    for mi, mtx in enumerate(matrixs):
        if mi in winMtx:
            continue
        for i, xy in enumerate(mtx):
            hsum = 0
            vsum = 0
            for j, x in enumerate(xy):
                if l == x:
                    xy[j] = -1
                hsum = hsum + mtx[i][j]
                vsum = vsum + mtx[j][i]
            if hsum == -5 or vsum == -5:
                winMtx.add(mi)
            if len(winMtx) == len(matrixs):
                bk = True
                break
        if bk:
            resultMtx = mtx
            break
    if bk:
        finalNum = l
        break

mtxsum = 0
for xy in resultMtx:
    for x in xy:
        if x > -1:
            mtxsum = mtxsum + x


print(resultMtx)
print(finalNum, mtxsum, finalNum * mtxsum)
