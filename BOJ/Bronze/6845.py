for _ in range(int(input())):
    y, m, d = map(int, input().split())

    if (y < 1989 or
       (y == 1989 and m < 2) or
       (y == 1989 and m == 2 and d < 28)):
        print("Yes")
    else:
        print("No")

