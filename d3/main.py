file = open('inputs')

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

line = file.readline()

while line:
    for i, x in enumerate(line.replace('\n', '')):
        if int(x) == 1:
            lst[i] = lst[i] + 1
        else:
            lst[i] = lst[i] - 1

    line = file.readline()

file.close()


gamma = "";
epsilone = ""

for x in lst:
    if x > 0:
        gamma = gamma + "1"
        epsilone = epsilone + "0"
    else:
        gamma = gamma + "0"
        epsilone = epsilone + "1"


x = int(gamma, 2)
y = int(epsilone, 2)


print(gamma, epsilone, x, y)
print(x * y)