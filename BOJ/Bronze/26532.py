from math import ceil
w, h = map(int, input().split())

total = w * h / (4840 * 5)
print(ceil(total))