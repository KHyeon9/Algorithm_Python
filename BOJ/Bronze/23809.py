n = int(input())
for i in range(n * 5):
    if i // n == 0 or i // n == 4:
        print('@' * n + ' ' * n * 3 + '@' * n)
    elif i // n == 1 or i // n == 3:
        print('@' * n + ' ' * n * 2 + '@' * n)
    else:
        print('@' * 3 * n)