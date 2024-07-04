n, r, s = map(int, input().split())

for _ in range(n):
    max_val, min_val = 0, 1e9
    for i in range(r):
        line = input()

        if "#" in line:
            val = r - i
            max_val = max(max_val, val)
            min_val = min(max_val, val)

    print(max_val - min_val)
