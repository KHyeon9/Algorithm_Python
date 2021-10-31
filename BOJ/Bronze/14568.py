n = int(input())
cnt = 0
for i in range(2, n + 1, 2):
    for j in range(1, n + 1):
        c = n - i - j
        if c >= j + 2:
            cnt += 1
        else:
            break
print(cnt)