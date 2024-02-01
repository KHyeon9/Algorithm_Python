from math import ceil
for _ in range(int(input())):
    n, s = map(int, input().split())
    s_max = max(list(map(int, input().split())))

    print(ceil((s_max * s) / 1000))
