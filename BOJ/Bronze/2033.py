n = int(input())
c = 1
while n > pow(10, c):
    if n % pow(10, c) >= pow(10, c) // 2:
        n += pow(10, c)
    n -= n % pow(10, c)
    c += 1
print(n)

