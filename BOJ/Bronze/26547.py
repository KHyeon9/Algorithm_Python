for _ in range(int(input())):
    s = input()
    l = len(s)

    if l == 1:
        print(s)
        continue

    print(s)
    for i in range(1, l - 1):
        print(s[i] + " " * (l - 2) + s[-i - 1])
    print(s[::-1])