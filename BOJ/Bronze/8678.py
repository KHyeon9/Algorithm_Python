from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())

    print("TAK" if b % a == 0 else "NIE")