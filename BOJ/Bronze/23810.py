n = int(input())
for i in range(3):
    if i % 2 == 0:
        for j in range(n):
            print('@' * n * 5)
    else:
        for j in range(n):
            print('@' * n)
for i in range(n * 2):
    print('@' * n)