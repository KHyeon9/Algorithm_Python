from sys import stdin
for _ in range(int(stdin.readline())):
    a, b, c = map(int, stdin.readline().split())
    arr = [a + b, abs(a - b), a * b, a / b, b / a]
    print('Possible' if c in arr else 'Impossible')