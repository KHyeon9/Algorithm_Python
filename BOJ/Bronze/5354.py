t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("#" * n)
        else:
            print("#" + "J" * (n - 2) + "#")

    print()