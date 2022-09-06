num = input()
arr = []

while 1:
    r = 0
    for i in num:
        r += int(i) ** 2

    if r in arr:
        break
    else:
        arr.append(r)
        num = str(r)
print("HAPPY" if 1 in arr else "UNHAPPY")