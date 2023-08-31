for t in range(int(input())):
    n = int(input())
    guests = list(map(int, input().split()))
    res = 0

    for g in set(guests):
        if guests.count(g) == 1:
            res = g
            break

    print(f"Case #{t + 1}: {res}")