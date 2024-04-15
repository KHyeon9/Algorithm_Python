from sys import stdin
arr = []
res = 0
for i in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())

    if i > 0:
        if arr[i - 1][0] == a and arr[i - 1][0] != 0:
            res += 1
        if arr[i - 1][1] == b and arr[i - 1][1] != 0:
            res += 1

    if a == b and a != 0:
        res += 1

    arr.append([a, b])

print(res)