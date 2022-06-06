while 1:
    manggo = list(map(int, input().split()))

    if manggo[0] == 0:
        break
    result = []
    for i in manggo[1:]:
        if len(result) != 0 and result[-1] == i:
            continue
        result.append(i)
    result.append('$')
    print(*result)