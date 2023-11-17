for t in range(int(input())):
    n, m, p = map(int, input().split())
    steps = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for day in range(m):
        max_step = 0
        for id in range(n):
            if p - 1 != id:
                max_step = max(steps[id][day], max_step)

        res += max(0, max_step - steps[p - 1][day])

    print(f"Case #{t + 1}: {res}")


