from math import sqrt
i = 1
while 1:
    rwl = list(map(int, input().split()))

    if rwl[0] == 0:
        break
    l = sqrt(rwl[1] ** 2 + rwl[2] ** 2) / 2
    if l <= rwl[0]:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")
    i += 1