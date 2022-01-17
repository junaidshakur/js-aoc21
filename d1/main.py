
inputFile = open("inputs")

lst = []

line = inputFile.readline()
while line:
    lst.append(int(line))
    line = inputFile.readline()

inputFile.close()


inc = 0;
lastVal = 999999999999999;
for x in lst:
    if x > lastVal:
        inc = inc + 1
    lastVal = x

print(inc)
