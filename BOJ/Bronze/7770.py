n = int(input())
h, block = 1, 0
while block <= n:
    block += h ** 2 + (h - 1) ** 2
    h += 1
print(h - 2)