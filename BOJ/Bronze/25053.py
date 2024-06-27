for _ in range(int(input())):
    arr = [0] * 10

    for _ in range(int(input())):
        b, d = map(int, input().split())
        arr[d - 1] = max(arr[d - 1], b)

    if 0 in arr:
        print("MOREPROBLEMS")
    else:
        print(sum(arr))