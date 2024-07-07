for _ in range(int(input())):
    n, m = map(int, input().split())
    counts = [0] * 101
    train1 = list(map(int, input().split()))
    train2 = list(map(int, input().split()))
    res = 0

    for el in train2:
        if el in train1:
            res += 1

    print(res)

