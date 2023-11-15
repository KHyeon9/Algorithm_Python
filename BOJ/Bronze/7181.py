n = input()
for _ in range(int(input())):
    in_n = input()
    a, b = 0, 0

    for i in range(len(n)):
        if n[i] == in_n[i]:
            a += 1
            b += 1

        elif in_n[i] in n:
            a += 1

    print(a, b)