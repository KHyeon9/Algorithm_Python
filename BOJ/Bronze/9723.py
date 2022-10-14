for i in range(int(input())):
    tri = sorted(list(map(int, input().split())))
    res = "NO"
    if tri[-1] ** 2 == tri[0] ** 2 + tri[1] ** 2:
        res = "YES"
    print(f"Case #{i + 1}: {res}")