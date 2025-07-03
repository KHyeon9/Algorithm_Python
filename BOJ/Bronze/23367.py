left = "qwertasdfgzxcvb"
right = "yuiophjklnm"

line = input()
flag = True if line[0] in left else False

for i in range(1, len(line)):
    if (flag and line[i] not in right) or (not flag and line[i] not in left):
        print("no")
        exit()
    flag = not flag
print("yes")