from functools import reduce


file = open('inputs')
lst = []
res = 0

line = file.readline()
while line:
    ls = [int(x) for x in line.replace('\n', '')]
    lst.append(ls)
    line = file.readline()
file.close()

xlen = len(lst) - 1
ylen = len(lst[0]) - 1

stk = []
ni = []
result = []
cA = 0

i, j = 0, 0
        
for i in range(len(lst)):
    for j in range(len(lst[i])):
        n = lst[i][j]
        nc = 0

        if n == 9 or n == -1:
            continue

        stk.append((i, j))
        while len(stk) > 0:
            u, d, l, r = 9, 9, 9, 9
            
            si, sj = stk.pop()
            lst[si][sj] = -1
            nc = nc + 1

            if si - 1 >= 0:
                u = lst[si-1][sj]
                if u >-1 and u < 9:
                    stk.append((si-1, sj))
                    lst[si-1][sj] = -1

            if si+1 <= xlen:
                d = lst[si+1][sj]
                if d > -1 and d < 9:
                    stk.append((si + 1, sj))
                    lst[si+1][sj] = -1

            if sj - 1 >= 0:
                l = lst[si][sj-1]
                if l > -1 and l < 9:
                    stk.append((si, sj-1))
                    lst[si][sj-1] = -1

            if sj + 1 <= ylen:
                r = lst[si][sj+1]
                if r > -1 and r < 9:
                    stk.append((si, sj + 1))
                    lst[si][sj+1] = -1
            

        if nc > 0:
            result.append(nc)
        #print("-----------")
        # print(result)

result.sort(lambda a,b: (b - a))

print(reduce(lambda s, x: s * x, result[:3]))
print(result)
