r, c, zr, zc = map(int, input().split())
result = []
for _ in range(r):
    s = input()
    for i in range(zr):
        for j in s:
            print(j * zc, end='')
        print()
