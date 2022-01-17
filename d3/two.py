from typing import KeysView


file = open('inputs')

#lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

c = 0
nums = []
ones = []
zeros = []

line = file.readline()

while line:
    line = line.replace('\n', '')
    if line[0] == '1':
        c = c + 1
        ones.append(line)
    else:
        c = c - 1
        zeros.append(line)

    line = file.readline()

file.close()


if c >= 0:
    nums = list(ones)
    #nums = list(zeros)
else:
    nums = list(zeros)
    #nums = list(ones)

ones.clear()
zeros.clear()

i = 1
c = 0
totalLen = len(nums[0])

while True:
    if(i >= totalLen):
        break
    for x in nums:
        if x[i] == "1":
            c = c + 1
            ones.append(x)
        else:
            c = c - 1
            zeros.append(x)
    
    #if c >= 0 and len(zeros) > 0:
    if c >= 0 and len(ones) > 0:
        nums = list(ones)
        #nums = list(zeros)
        ones.clear()
        zeros.clear()
    #elif c < 0 and len(ones) > 0:
    elif c < 0 and len(zeros) > 0:
        nums = list(zeros)
        #nums = list(ones)
        ones.clear()
        zeros.clear()
    else:
        break
    i = i + 1
    c = 0

print("i, c, ones, zeros, numes: ", i, c, ones, zeros, nums)
 

# print(nums)
# print(ones)
# print(zeros)

# i = 0

# oxdic = {}
# codic = {}

# for i, x in enumerate(nums):
#     p = 0
#     q = 0
#     for j, b in enumerate(x):
#         if (lst[j] >= 0 and b == "1") or (lst[j] < 0 and b == "0"):
#             p = p + 1
#         else:
#             break
#     for j, b in enumerate(x):
#         if (lst[j] >= 0 and b == "0") or (lst[j] < 0 and b == "1"):
#             q = q + 1
#         else:
#             break
#     oxdic[i] = p
#     codic[i] = q

# print(lst)
# print(sorted(oxdic.items(), key=lambda x: x[1]))
# print(sorted(codic.items(), key=lambda x: x[1]))
