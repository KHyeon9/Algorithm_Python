for _ in range(int(input())):
    n, c, s = input().split()

    for _ in range(int(c)):
        s = s[int(n):] + s

    print(s)