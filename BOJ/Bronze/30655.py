from sys import stdin

while True:
    n, m = map(int, stdin.readline().split())

    if n == m == 0:
        break

    arr = [int(stdin.readline()) for _ in range(n - 2)]
    arr.append(m)

    for i in range(1, n + 1):
        if i not in arr:
            print(i)
            break
