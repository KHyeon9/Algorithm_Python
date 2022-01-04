r = 0
for _ in range(3):
    num = input()
    cnt = 1
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if r < cnt:
            r = cnt
    print(r)
    r = 0