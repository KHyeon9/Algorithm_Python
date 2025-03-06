from math import ceil

t = 0
while True:
    s = int(input())

    if s == 0:
        break

    t += 1
    res = ceil(s / 2)
    res = ceil(res * 1.5)
    res = ceil(res / 1860000)

    print(f"File #{t}")
    print(f"John needs {res} floppies.")
    print()

