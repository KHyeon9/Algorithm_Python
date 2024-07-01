from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    media = set(input().strip("\n"))
    res = 0

    for _ in range(n):
        line = input()
        for el in media:
            if el in line:
                res += 1
                break

    print(f"Data Set {t + 1}:")
    print(res)
    print()

