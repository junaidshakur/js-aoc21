import re

file = open('inputs')

line = file.readline()
mtx = []
while line:
    mtx.append(filter(bool, re.split(' |\|', line.replace('\n', ''))))
    line = file.readline()
file.close()

res = 0
counter = 0
for x in mtx:
    
    result = ""
    one = ""
    four = ""
    seven = ""
    eight = ""
    for y in x[0:10]:
        ll = len(y)
        if ll == 2:
            one = y
        elif ll == 3:
            seven = y
        elif ll == 4:
            four = y
        elif ll == 7:
            eight = y

    for y in x[10:]:
        
        ll = len(y)
        #print(y, ll)
        if ll == 2:
            result = result + "1"
        elif ll == 3:
            result = result + "7"
        elif ll == 4:
            result = result + "4"
        elif ll == 7:
            result = result + "8"
        elif ll == 6:
            found = True
            for i in four:
                if i in y:
                    continue
                else:
                    found = False
                    break
            if found:
                result = result + "9"
            else:
                found = True
                for i in one:
                    if i in y:
                        continue
                    else:
                        found = False
                        break
                if found:
                    result = result + "0"
                else:
                    result = result + "6"
        elif ll == 5:
            found = True
            for i in seven:
                if i in y:
                    continue
                else:
                    found = False
                    break
            if found:
                result = result + "3"
            else:
                foundCount = 0
                for i in four:
                    if i in y:
                        foundCount = foundCount + 1
                        continue
                if foundCount == 3:
                    result = result + "5"
                else:
                    result = result + "2"
    
    #print(result)
    res = res + int(result)

print("Sum is: ", res)
