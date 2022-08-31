s = input()

for i in s:
    cnt = str(ord(i))
    S = 0
    for j in cnt:
        S += int(j)
    print(i * S)
