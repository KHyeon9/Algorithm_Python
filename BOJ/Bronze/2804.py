a, b = input().split()
for i in range(len(a)):
    if a[i] in b:
        num = i
        row = b.index(a[i])
        break
for i in range(len(b)):
    if i == row:
        print(a)
    else:
        print('.' * num + b[i] + '.' * (len(a) - num - 1))

