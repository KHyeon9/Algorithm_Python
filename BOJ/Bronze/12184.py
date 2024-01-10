for t in range(1, int(input()) + 1):
    if t != 1:
        input()
    n = int(input())
    bus = list(map(int, input().split()))
    c = int(input())
    res = []

    for _ in range(c):
        p = int(input())
        cnt = 0
        for i in range(0, n * 2, 2):
            if bus[i] <= p <= bus[i + 1]:
               cnt += 1

        res.append(cnt)

    print(f"Case #{t}: ", end="")
    print(*res)

