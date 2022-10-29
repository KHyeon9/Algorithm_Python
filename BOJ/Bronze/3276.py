n = int(input())
a, b = 1, 1
while a * b < n:
    if a > b:
        b += 1
        continue
    a += 1
print(a, b)