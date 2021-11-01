r1 = 0

for i in range(9):
    n = list(map(int, input().split()))

    if max(n) > r1:
        r1 = max(n)
        x = i + 1

        for j in range(9):
            if r1 == n[j]:
                y = j + 1

print(r1)
print(x, y)