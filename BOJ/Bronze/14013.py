from sys import stdin
x, y = map(float, stdin.readline().split())
for _ in range(int(stdin.readline())):
    dudu = input()
    duduNum = float(dudu[:-1])
    if dudu[-1] == 'A':
        print(duduNum / x * y)
    else:
        print(duduNum / y * x)