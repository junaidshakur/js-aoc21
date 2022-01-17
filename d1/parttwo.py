
inputFile = open("inputs")
lst = [0, 0]
i = 0
line = inputFile.readline()
while line:
    a = int(line)
    lst[i] = lst[i] + a
    lst[i + 1] = lst[i + 1] + a
    lst.append(a)

    line = inputFile.readline()
    i = i + 1

inputFile.close()

#print(lst)

total = len(lst)

inc = 0
lastVal = 999999999999999

for x in lst[2:]:
    if x > lastVal:
        inc = inc + 1
    lastVal = x

#print(newlst)
print(inc)
