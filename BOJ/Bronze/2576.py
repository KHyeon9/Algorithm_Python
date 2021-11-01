r1 = 0
r2 = 100

for i in range(7):
    n = int(input())

    if n % 2 != 0:
        r1 += n

        if r2 > n:
            r2 = n

if r1 == 0:
    print(-1)

else:
    print(r1, r2)