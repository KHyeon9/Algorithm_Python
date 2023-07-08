while True:
    arr = []
    res = ""
    glued = list(input().split())
    if glued[0] == "#":
        break

    for i in range(1, len(glued[1])):
        if glued[1][i] == glued[1][i - 1] and glued[1][i] not in arr:
            arr.append(glued[1][i])
    if len(arr) == 0:
        continue
    for i in range(len(arr)):
        if i == 0:
            res += f"{arr[i]} {arr[i]} glued"
        else:
            res += f" and {arr[i]} {arr[i]} glued"
    print(res)