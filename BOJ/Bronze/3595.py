n = int(input())
MIN = 1e9

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j > n:
            break
        for k in range(1, n + 1):
            if i * j * k > n:
                break
            if i * j * k < n:
                continue
            temp = i * j + i * k + j * k
            if MIN > temp and i * j * k == n:
                MIN = temp
                a, b, c = i, j, k

print(a, b, c)
