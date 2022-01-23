n = int(input())

for i in range(n):
    if i == n - 1:
        print("*" * (2 * n - 1))

    else:
        if i == 0:
            print(" " * (n - i - 1) + "*")
        else:
            print(" " * (n - 1 - i) + "*" + " " * (i * 2 - 1) + "*")