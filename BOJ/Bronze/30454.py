res, cnt = 0, 0

n, l = map(int, input().split())

for _ in range(n):
    line = input()
    flag = False
    black_line = 0

    for i in line:
        if i == "1" and not flag:
            flag = True

        if i == "0" and flag:
            flag = False
            black_line += 1

    if line[-1] == "1":
        black_line += 1

    if res == black_line:
        cnt += 1

    elif res < black_line:
        res = black_line
        cnt = 1

print(res, cnt)
