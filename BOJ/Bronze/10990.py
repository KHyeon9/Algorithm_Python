n = int(input())

for i in range(n):
    if i == 0:
        print(" " * (n - 1) + "*")

    else:
        print(" " * (n - i - 1) + "*" + " " * (i * 2 - 1) + "*")