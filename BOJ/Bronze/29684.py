while True:
    n = int(input())

    if n == 0:
        break

    min_val = 1e9
    data_set = list(map(int, input().split()))
    res = 1

    for i in range(len(data_set)):
        if abs(data_set[i] - 2023) < min_val:
            min_val = abs(data_set[i] - 2023)
            res = i + 1

    print(res)
