while True:
    n = input()
    l = 0

    if n == "0":
        break

    for i in range(len(n)):
        if n[i] == "0":
            l += 4

        elif n[i] == "1":
            l += 2

        else:
            l += 3

    print(l + 2 + int(len(n)) - 1)