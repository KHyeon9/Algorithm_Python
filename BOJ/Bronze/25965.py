for _ in range(int(input())):
    res = 0
    mission = [list(map(int, input().split())) for _ in range(int(input()))]
    my_k, my_d, my_a = map(int, input().split())

    for k, d, a in mission:
        total = my_k * k - my_d * d + my_a * a
        if total < 0:
            continue

        res += total

    print(res)
