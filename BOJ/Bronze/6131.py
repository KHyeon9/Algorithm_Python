n = int(input())
r = 0

for i in range(1, 501):
    for j in range(1, 501):
        r1 = i ** 2
        r2 = j ** 2
        if r1 - r2 == n:
            r += 1

print(r)