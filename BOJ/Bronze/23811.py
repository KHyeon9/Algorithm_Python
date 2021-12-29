n = int(input())
for i in range(5):
    if i % 2 == 0:
        for _ in range(n):
            print('@' * 5 * n)
    else:
        for _ in range(n):
            print('@' * n)
