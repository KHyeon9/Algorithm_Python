n = int(input())
r = 0

if n < 199:
    for i in range(1, 100):
        for j in range(1, 100):
            num = n - i - j

            if num == 0:
                r += 1

print(r)