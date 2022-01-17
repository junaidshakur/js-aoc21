
inputFile = open("inputs")

line = inputFile.readline()

position = 0
depth = 0
aim = 0

while line:
    ss = line.replace("\n", "").split(" ")
    cmd = ss[0]
    val = int(ss[1])
    
    if cmd == "forward":
        position = position + val
        depth = depth + (aim * val)
    elif cmd == "up":
        aim = aim - val
    elif cmd == "down":
        aim = aim + val

    line= inputFile.readline()

inputFile.close()


print(position * depth)
