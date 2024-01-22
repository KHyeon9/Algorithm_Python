for _ in range(int(input())):
    line = input()
    res = line
    for i in range(len(line)):
        temp = line[i:] + line[:i]
        if res > temp:
            res = temp

    print(res)