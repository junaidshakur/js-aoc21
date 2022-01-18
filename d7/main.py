import functools

file = open('inputs')

line = file.readline()
lst = list(map(int, line.replace('\n', '').split(',')))
file.close()

lst.sort()

print(sum(lst))

minValue = 999999999999999999999
minNum = 0
offset = 0

sumM = 0
sumML = 0
sumMR = 0

start = 0
end = len(lst) - 1
pi = 0
midI = 0
midLI = 0
midRI = 0

#print(lst)

while True:
    
    pi = start + abs((end - start) / 2)
    midI = pi
    midLI = pi
    midRI = pi
    sumM = 0
    sumML = 0
    sumMR = 0

    while True: 
        if lst[pi] == lst[midLI]:
            midLI = midLI - 1
            if midLI < start:
                midLI = start
                break
        else:
            break

    while True:
        if lst[pi] == lst[midRI]:
            midRI = midRI + 1
            if midRI > end:
                midRI = end
                break
        else:
            break

    print("indexs", start, end, pi, midLI, midI, midRI)
    print("Index Value:", lst[midLI], lst[midI], lst[midRI])

    if midRI == end and midLI == start:
        break

    for i in range(len(lst)):
        diff = abs(lst[i] - lst[pi])
        diffL = abs(lst[i] - lst[midLI])
        diffR = abs(lst[i] - lst[midRI])
        sumM = sumM + ((diff*(diff + 1)) / 2)
        sumML = sumML + ((diffL*(diffL + 1)) / 2)
        sumMR = sumMR + ((diffR*(diffR + 1)) / 2)


    print("Sums: ", sumML, sumM, sumMR)

    if minValue > min(sumM, sumML, sumMR):
        minValue = min(sumM, sumML, sumMR)

    if sumM < sumML and sumM < sumMR:
        if minValue > sumM:
            minValue = sumM
            minNum = lst[pi]
        break
    elif sumML < sumMR:
        end = midLI
    elif sumMR > sumML:
        start = midRI
    else:
        start = midRI
    


print(minValue)
print(minNum)
#print(lst)
