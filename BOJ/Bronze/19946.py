n = int(input())
i = 64
while 1:
    if n % 2 == 1:
        break
    n //= 2
    i -= 1
print(i)