for t in range(int(input())):
    e, a = map(int, input().split())

    print(f"Data Set {t + 1}:")

    if e <= a:
        print("no drought")
    else:
        n = -1
        temp = e / a

        while temp > 1:
            temp /= 5
            n += 1

        print("mega " * n + "drought")
    print()
