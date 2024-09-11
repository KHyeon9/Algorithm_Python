from sys import stdin

for _ in range(int(stdin.readline())):
    num = list(map(int, list(stdin.readline().strip())))
    res = sum(num)

    print("YES" if res % 9 == 0 else "NO")