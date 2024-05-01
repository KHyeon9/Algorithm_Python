n = int(input())
ignore_defence = list(map(int, input().split()))
res = 0

for posion in ignore_defence:
    res += (100 - res) * (posion / 100)
    print(res)
