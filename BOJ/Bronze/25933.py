for _ in range(int(input())):
    total_set = list(map(int, input().split()))
    usa = total_set[:3]
    rua = total_set[3:]
    count = sum(usa) > sum(rua)
    color = False

    for i in range(3):
        if usa[i] > rua[i]:
            color = True
            break
        elif usa[i] < rua[i]:
            break
        else:
            continue

    if color and count:
        res = "both"
    elif color and not count:
        res = "color"
    elif not color and count:
        res = "count"
    else:
        res = "none"

    print(*total_set)
    print(res)
    print()
