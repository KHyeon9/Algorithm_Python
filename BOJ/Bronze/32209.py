res = 0
flag = True
for _ in range(int(input())):
    n, xy = map(int, input().split())
    res += xy if n == 1 else -xy

    if res < 0:
        flag = False

print("See you next month" if flag else "Adios")