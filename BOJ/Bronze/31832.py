res = ""

for _ in range(int(input())):
    s = input()
    if len(s) > 10:
        continue

    upper, lower = 0, 0
    digit = 0

    for ch in s:
        if ch.isdigit():
            digit += 1
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1

    if lower >= upper and digit != len(s):
        res = s
print(res)

