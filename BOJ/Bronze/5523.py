from sys import stdin
n = int(stdin.readline())
r1 = r2 = 0

for i in range(n):
    point = list(map(int, stdin.readline().split()))

    if point[0] > point[1]:
        r1 += 1

    elif point[1] > point[0]:
        r2 += 1

print(r1, r2)