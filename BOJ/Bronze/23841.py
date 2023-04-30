n, m = map(int, input().split())
res = []
for _ in range(n):
    s = input()
    left = list(s[:m // 2])
    right = list(s[m//2:])
    for i in range(m // 2):
        if left[i] != '.':
            right[-i - 1] = left[i]
        if right[i] != '.':
            left[-i - 1] = right[i]

    res.append(left + right)
for i in res:
    print(*i, sep='')