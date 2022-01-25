file = open('inputs')

lst = []
line = file.readline()
while line:
    lst.append(list(map(int, line.replace('\n', ''))))
    line= file.readline()
file.close()


fC = 0
stk = []
step = 0

while True:
    step += 1
    lastFC = fC
    for i,x in enumerate(lst):
        for j,y in enumerate(x):
            lst[i][j] += 1
            if lst[i][j] == 10:
                lst[i][j] = 0
                fC += 1
                stk.append((i, j))

    # if len(stk) == 10 * 10:
    #     break

    #print(stk)
    while len(stk) > 0:
        x, y = stk.pop()
        #top left
        if x-1 >= 0 and y-1 >= 0:
            if lst[x-1][y-1] > 0:
                lst[x-1][y-1] +=1
            if lst[x-1][y-1] > 9:
                lst[x-1][y-1] =0
                fC +=1
                stk.append((x-1, y-1))


        #top
        if x-1 >= 0:
            if lst[x-1][y] > 0:
                lst[x-1][y] += 1
            if lst[x-1][y] > 9:
                lst[x-1][y] =0
                fC +=1
                stk.append((x-1, y))
            

        #top right
        if x-1 >= 0 and y+1 < 10:
            if lst[x-1][y+1] > 0:
                lst[x-1][y+1] += 1
            if lst[x-1][y+1] > 9:
                lst[x-1][y+1] =0
                fC +=1
                stk.append((x-1, y+1))
        
        #left
        if y-1 >= 0:
            if lst[x][y-1] > 0:
                lst[x][y-1] += 1
            if lst[x][y-1] > 9:
                lst[x][y-1] =0
                fC +=1
                stk.append((x,y-1))

        #right
        if y+1 < 10:
            if lst[x][y+1] > 0:
                lst[x][y+1] += 1
            if lst[x][y+1] > 9:
                lst[x][y+1] =0
                fC +=1
                stk.append((x, y+1))

        #bottom left
        if x+1 < 10 and y-1 >= 0:
            if lst[x+1][y-1] > 0:
                lst[x+1][y-1] +=1
            if lst[x+1][y-1] > 9:
                lst[x+1][y-1] =0
                fC +=1
                stk.append((x+1,y-1))

        #bottom
        if x+1 < 10:
            if lst[x+1][y] > 0:
                lst[x+1][y] +=1
            if lst[x+1][y] > 9:
                lst[x+1][y] =0
                fC +=1
                stk.append((x+1,y))


        #bottom right
        if x+1<10 and y+1<10:
            if lst[x+1][y+1] > 0:
                lst[x+1][y+1] +=1
            if lst[x+1][y+1] > 9:
                lst[x+1][y+1] =0
                fC +=1
                stk.append((x+1,y+1))

    if fC - lastFC == 10 * 10:
        break

print(step)
print(fC)
print(lst)