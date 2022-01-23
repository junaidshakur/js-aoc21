
dic = {"}": "{", ")": "(", "]": "[", ">":"<" }

lst = []
file = open('inputs')

line = file.readline()
while line:
    lst.append(line.replace('\n', ''))
    line = file.readline()
file.close()

nc = 0
lst2 = []

for str in lst:
    nc2 = 0
    incorrect = False
    stk = []
    for c in str:
        if c in ["(", "{", "[", "<"]:
            stk.append(c)
        else:
            ex = dic[c]
            if ex == stk[-1]:
                stk.pop()
                continue
            else:
                if ex == "(":
                    nc = nc + 3
                elif ex == "[":
                    nc = nc + 57
                elif ex == "{":
                    nc = nc + 1197
                elif ex == "<":
                    nc = nc + 25137
                incorrect = True
                break

    if incorrect:
        continue

    while len(stk) > 0:
        nc2 = nc2 * 5
        ex = stk.pop()
        if ex == "(":
            nc2 = nc2 + 1
        elif ex == "[":
            nc2 = nc2 + 2
        elif ex == "{":
            nc2 = nc2 + 3
        elif ex == "<":
            nc2 = nc2 + 4
    
    lst2.append(nc2)

lst2.sort(lambda a, b: (a - b))

print(nc)
print(lst2)
print(lst2[len(lst2)/2])
