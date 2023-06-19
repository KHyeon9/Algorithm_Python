points = {'A': 4, 'K': 3, 'Q': 2, 'J': 1, 'X': 0}
res = 0

for _ in range(int(input())):
    s = input()

    for i in s:
        res += points[i]
print(res)
