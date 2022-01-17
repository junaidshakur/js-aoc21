
file = open('inputs')

line = file.readline()

lst = []
while line:
    lst = map(int, line.replace('\n', '').split(','))
    line = file.readline()
file.close()


# for i in range(80):
#     for j in range(len(lst)):
#         lst[j] = lst[j] - 1
#         if lst[j] == -1:
#             lst[j] = 6
#             lst.append(8)

def getAns(n):
    b = 0
    if res.get(n):
        return res.get(n)

    if (n-7) > 0:
        b = b + getAns(n-7)
        b = b + getAns(n-9)
    else:
        b = b + 1
    
    res[n] = b
    return b

total = 0
res = {}
stk = []
for x in lst:
    x = (6 - x) + (256 + 1)
    total = total + getAns(x)

#print(stk)

# while len(stk) > 0:
#     n = stk.pop()
#     if (n - 7) > 0:
#         stk.append(n - 7)
#         stk.append(n - 9)        
#     else:
#         total = total +1
    


#print(stk)
print(total)