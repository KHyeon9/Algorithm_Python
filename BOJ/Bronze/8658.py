n = int(input())
tmp = 2

while 1:
    if n % tmp != 0:
        print(tmp, n - 1)
        break
    tmp += 1