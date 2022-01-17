from operator import truediv
import re

file = open('inputs')

line = file.readline()

dic = {}
x1, y1, x2, y2 = 0, 0, 0, 0
while line:
    #print(line)
    result = re.search('(\d+),(\d+) -> (\d+),(\d+)', line.replace('\n', ''), re.IGNORECASE)
    x1, y1, x2, y2 = map(int, result.groups())
    if x1 == x2 or y1 == y2:

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        
        #print(x1, x2, y1, y2)
        
        while True:
            p = str(x1) + ":" + str(y1)
            #print(p)
            if dic.get(p):
                dic[p] = dic[p] + 1
            else:
                dic[p] = 1

            if x1 == x2:
                y1 = y1 + 1
            else:
                x1 = x1 + 1

            if x1 > x2 or y1 > y2:
                break
    elif abs(x1 - x2) == abs(y1 - y2):
        #print(x1, y1, x2, y2)
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        while True:
            p = str(x1) + ":" + str(y1)
            #print(p)
            if dic.get(p):
                dic[p] = dic[p] + 1
            else:
                dic[p] = 1

            if x1 == x2 and y1 == y2:
                break
            x1 = x1 + 1
            if y1 < y2:
                y1 = y1 + 1
            else:
                y1 = y1 - 1
            

    line = file.readline()
file.close()

result = 0;
for v in dic.values():
    if v >= 2:
        result = result + 1
    
    
#print(dic)
print(result)
