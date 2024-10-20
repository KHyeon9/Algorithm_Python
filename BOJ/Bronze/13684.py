while True:
    k = int(input())

    if k == 0:
        break

    n, m = map(int, input().split())

    for _ in range(k):
        x, y = map(int, input().split())

        if x == n or y == m:
            print("divisa")

        else:
            res = ("S" if y < m else "N") + ("O" if x < n else "E")
            print(res)