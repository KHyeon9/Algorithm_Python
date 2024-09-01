from sys import stdin

total = 0

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    total = a - b + total
    print(total)